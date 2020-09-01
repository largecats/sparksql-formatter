# -*- coding: utf-8 -*-
# MIT License

# Copyright (c) 2016-present ZeroTurnaround LLC
# Copyright (c) 2016-present kufii
# Copyright (c) 2020-present largecats

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
from __future__ import print_function  # for print() in Python 2
import re

import sparksqlformatter.src.config as config


class TokenType:
    '''
    Different types of tokens.
    '''
    WHITESPACE = 'WHITESPACE'
    WORD = 'WORD'
    KEYWORD = 'KEYWORD'
    STRING = 'STRING'
    RESERVED_KEYWORD = 'RESERVED_KEYWORD'
    TOP_LEVEL_KEYWORD = 'TOP_LEVEL_KEYWORD'
    TOP_LEVEL_KEYWORD_NO_INDENT = 'TOP_LEVEL_KEYWORD_NO_INDENT'
    NEWLINE_KEYWORD = 'NEWLINE_KEYWORD'
    OPERATOR = 'OPERATOR'
    OPEN_PAREN = 'OPEN_PAREN'
    CLOSE_PAREN = 'CLOSE_PAREN'
    LINE_COMMENT = 'LINE_COMMENT'
    BLOCK_COMMENT = 'BLOCK_COMMENT'
    NUMBER = 'NUMBER'


class Token:
    '''
    A token is a string that forms a unit in formatting.
    '''
    def __init__(self, type, value, flag=None):
        __slots__ = 'type', 'value', 'flag'  # saves space since there would be many instances of Token
        self.type = type
        self.value = value
        self.flag = flag  # added by formatter.py when formatting


class Tokenizer:
    def __init__(self, style):
        self.WHITESPACE_REGEX = u'^(\s+)'
        self.NUMBER_REGEX = r'^((-\s*)?[0-9]+(\.[0-9]+)?|0x[0-9a-fA-F]+|0b[01]+)\b'
        self.OPERATOR_REGEX = u'^([^\{\}]!=|<>|==|<=|>=|!=|!<|!>|\|\||::|->>|->|~~\*|~~|!~~\*|!~~|~\*|!~\*|!~|:=|.)'

        self.BLOCK_COMMENT_REGEX = u'(\/\*(?s).*?\*\/)'  # (?s) is inline flag for re.DOTALL
        self.LINE_COMMENT_REGEX = Tokenizer.create_line_comment_regex(style.lineCommentTypes)

        self.TOP_LEVEL_KEYWORD_REGEX = Tokenizer.create_keyword_regex(style.topLevelKeywords)
        self.TOP_LEVEL_KEYWORD_NO_INDENT_REGEX = Tokenizer.create_keyword_regex(style.topLevelKeywordsNoIndent)
        self.NEWLINE_KEYWORD_REGEX = Tokenizer.create_keyword_regex(style.newlineKeywords)
        self.RESERVED_KEYWORD_REGEX = Tokenizer.create_keyword_regex(config.Keyword.RESERVED_KEYWORDS)
        self.PLAIN_KEYWORD_REGEX = Tokenizer.create_keyword_regex(
            config.Keyword.RESERVED_KEYWORDS + config.Keyword.NON_RESERVED_KEYWORDS +
            config.Function.AGGREGATE_FUNCTIONS + config.Function.ARRAY_FUNCTIONS +
            config.Function.CONDITIONAL_FUNCTIONS + config.Function.DATE_TIME_FUNCTIONS +
            config.Function.HASH_FUNCTIONS + config.Function.JSON_FUNCTIONS + config.Function.MAP_FUNCTIONS +
            config.Function.MATHEMATICAL_FUNCTIONS + config.Function.MISC_FUNCTIONS +
            config.Function.OPERATOR_FUNCTIONS + config.Function.STRING_FUNCTIONS + config.Function.STRUCT_FUNCTIONS +
            config.Function.TABLE_GENERATING_FUNCTIONS + config.Function.TYPE_CONVERSION_FUNCTIONS +
            config.Function.WINDOW_FUNCTIONS + config.Function.XPATH_FUNCTIONS + style.userDefinedFunctions)

        self.WORD_REGEX = Tokenizer.create_word_regex(style.specialWordChars)
        self.STRING_REGEX = Tokenizer.create_string_regex(style.stringTypes)

        self.OPEN_PAREN_REGEX = Tokenizer.create_paren_regex(style.openParens)
        self.CLOSE_PAREN_REGEX = Tokenizer.create_paren_regex(style.closeParens)

    @staticmethod
    def create_line_comment_regex(lineCommentTypes):
        '''
        Create regex pattern that matches line comments in the query.

        Parameters
        lineCommentTypes: list
            Attribute of hiveqlformatter.src.style.Style() object.
        
        Return: string
            Regex pattern that matches line comment.
        '''
        lineCommentTypesString = ('|').join(list(map(lambda c: re.escape(c), lineCommentTypes)))
        regexString = u'^((?:{lineCommentTypesString}).*?(?:\r\n|\r|\n|$))'.format(
            lineCommentTypesString=lineCommentTypesString)
        return regexString

    @staticmethod
    def create_keyword_regex(keywords):
        '''
        Create regex pattern that matches keywords ikn the query.

        Parameters
        keywords: list
            Attribute of hiveqlformatter.src.style.Style() object.
        
        Return: string
            Regex pattern that matches keywords.
        '''
        keywordsString = ('|').join(keywords)
        keywordsPattern = re.sub(
            pattern=' ', repl='\\\s+', string=keywordsString
        )  # https://stackoverflow.com/questions/58328587/python-3-7-4-re-error-bad-escape-s-at-position-0
        regexString = u'^({keywordsPattern})\\b'.format(keywordsPattern=keywordsPattern)
        return regexString

    @staticmethod
    def create_word_regex(specialChars=[]):
        '''
        Create regex pattern that matches special characters in the query language.

        Parameters
        specialChars: list
            Attribute of hiveqlformatter.src.style.Style() object.
        
        Return: string
            Regex pattern that matches word with special characters.     
        '''
        specialCharsString = ('|').join(specialChars)
        regexString = u'^([\\w{specialCharsString}]+)'.format(specialCharsString=specialCharsString)
        return regexString

    @staticmethod
    def create_string_regex(stringTypes):
        '''
        Create regex pattern that matches strings in the query.

        Parameters
        stringTypes: list
            Attribute of hiveqlformatter.src.style.Style() object.
        
        Return: string
            Regex pattern that matches strings.    
        '''
        regexString = '^(' + Tokenizer.create_string_pattern(stringTypes) + ')'
        return regexString

    @staticmethod
    def create_string_pattern(stringTypes):
        '''This enables the following string patterns:
        1. curly bracket quoted python formatting keyword to be treated as string in hiveql formatting
        2. double quoted string using "" or \" to escape
        3. single quoted string using '' or \' to escape

        Parameters
        stringTypes: list
            Attribute of hiveqlformatter.src.style.Style() object.
        
        Return: string
            Regex pattern that matches strings.    
        '''
        patterns = {
            '{}': '(({[^}\\\\]*(?:\\\\.[^{\\\\]*)*(}|$))+)',
            '""': '(("[^"\\\\]*(?:\\\\.[^"\\\\]*)*("|$))+)',
            "''": "(('[^'\\\\]*(?:\\\\.[^'\\\\]*)*('|$))+)",
            '``': '((`[^`\\\\]*(?:\\\\.[^`\\\\]*)*(`|$))+)'
        }
        return ('|').join(list(map(lambda t: patterns[t], stringTypes)))

    @staticmethod
    def create_paren_regex(parens):
        '''
        Create regex pattern that matches parentheses in the query.

        Parameters
        parens: list
            Attribute of hiveqlformatter.src.style.Style() object.
        
        Return: string
            Regex pattern that matches parentheses.
        '''
        parensString = ('|').join(list(map(lambda p: Tokenizer.escape_paren(p), parens)))
        return '^(' + parensString + ')'

    @staticmethod
    def escape_paren(paren):
        '''
        Escape given parenthesis in regex pattern.

        Parameters
        paren: string
            The parenthesis to escape.
        
        Return: string
            Regex pattern with the parenthesis escaped.
        '''
        if (len(paren) == 1):
            return re.escape(paren)
        else:
            return '\\b' + paren + '\\b'

    def tokenize(self, input):
        """
        Takes a SQL string and breaks it into tokens.
        Each token is an object with type and value.

        Parameters
        input: string
            The query to format.
        
        Return: list
            Tokens extracted from the query.
        """
        if not input:
            return []

        tokens = []
        token = None
        while len(input):
            # Keep processing the string until it is empty
            token = self.get_next_token(input, token)  # get next token
            start = 0 if token is None else len(token.value)
            input = input[start::]  # advance thte string
            tokens.append(token)

        return tokens

    def get_next_token(self, input, previousToken):
        '''
        Find the next token object in given query.

        Parameters
        input: string
            The query to format.
        previousToken: Token() object
            The previous token found in the query.
        
        Return: Token() object
            The next token in the query.
        '''
        return (self.get_white_space_token(input) or self.get_comment_token(input) or self.get_string_token(input)
                or self.get_open_paren_token(input) or self.get_close_paren_token(input) or self.get_number_token(input)
                or self.get_keyword_token(input, previousToken) or self.get_word_token(input)
                or self.get_operator_token(input))

    def get_white_space_token(self, input):
        '''
        Find token of type TokenType.WHITESPACE in the query.

        Parameters
        input: string
            The query to format.
        
        Return: Token() object
            The identified white space token.
        '''
        return Tokenizer.get_token_on_first_match(input=input, type=TokenType.WHITESPACE, regex=self.WHITESPACE_REGEX)

    def get_comment_token(self, input):
        '''
        Find comment in the query.

        Parameters
        input: string
            The query to format.
        
        Return: Token() object
            The identified comment token.
        '''
        return self.get_line_comment_token(input) or self.get_block_comment_token(input)

    def get_line_comment_token(self, input):
        '''
        Find token of type TokenType.LINE_COMMENT in the query.

        Parameters
        input: string
            The query to format.
        
        Return: Token() object
            The identified line comment token.
        '''
        return Tokenizer.get_token_on_first_match(input=input,
                                                  type=TokenType.LINE_COMMENT,
                                                  regex=self.LINE_COMMENT_REGEX)

    def get_block_comment_token(self, input):
        '''
        Find token of type TokenType.BLOCK_COMMENT in the query.

        Parameters
        input: string
            The query to format.
        
        Return: Token() object
            The identified block comment token.
        '''
        return Tokenizer.get_token_on_first_match(input=input,
                                                  type=TokenType.BLOCK_COMMENT,
                                                  regex=self.BLOCK_COMMENT_REGEX)

    def get_string_token(self, input):
        '''
        Find token of type TokenType.STRING in the query.

        Parameters
        input: string
            The query to format.
        
        Return: Token() object
            The identified string token.
        '''
        return Tokenizer.get_token_on_first_match(input=input, type=TokenType.STRING, regex=self.STRING_REGEX)

    def get_open_paren_token(self, input):
        '''
        Find token of type TokenType.OPEN_PAREN in the query.

        Parameters
        input: string
            The query to format.
        
        Return: Token() object
            The identified opening parenthesis token.
        '''
        return Tokenizer.get_token_on_first_match(input=input, type=TokenType.OPEN_PAREN, regex=self.OPEN_PAREN_REGEX)

    def get_close_paren_token(self, input):
        '''
        Find token of type TokenType.CLOSE_PAREN in the query.

        Parameters
        input: string
            The query to format.
        
        Return: Token() object
            The identified closing parenthesis token.
        '''
        return Tokenizer.get_token_on_first_match(input=input, type=TokenType.CLOSE_PAREN, regex=self.CLOSE_PAREN_REGEX)

    def get_number_token(self, input):
        '''
        Find token of type TokenType.NUMBER in the query.

        Parameters
        input: string
            The query to format.
        
        Return: Token() object
            The identified  number token.
        '''
        return Tokenizer.get_token_on_first_match(input=input, type=TokenType.NUMBER, regex=self.NUMBER_REGEX)

    def get_operator_token(self, input):
        '''
        Find token of type TokenType.OPERATOR in the query.

        Parameters
        input: string
            The query to format.
        
        Return: Token() object
            The identified operator token.
        '''
        return Tokenizer.get_token_on_first_match(input=input, type=TokenType.OPERATOR, regex=self.OPERATOR_REGEX)

    def get_keyword_token(self, input, previousToken):
        """
        A keyword cannot be preceded by a "."
        This makes it so in "my_table.from", "from" is not considered a key word

        Find keyword token in the query.

        Parameters
        input: string
            The query to format.
        previousToken: Token() object
            The last identified token.
        
        Return: Token() object
            The identified keyword token.
        """
        if (previousToken and previousToken.value and previousToken.value == '.'):
            return
        return (self.get_top_level_keyword_token(input) or self.get_newline_keyword_token(input)
                or self.get_top_level_keyword_token_no_indent(input) or self.get_reserved_keyword_token(input)
                or self.get_plain_keyword_token(input))

    def get_reserved_keyword_token(self, input):
        '''
        Find token of type TokenType.RESERVED_KEYWORD in the query.

        Parameters
        input: string
            The query to format.
        
        Return: Token() object
            The identified reserved keyword token.
        '''
        return Tokenizer.get_token_on_first_match(input=input,
                                                  type=TokenType.RESERVED_KEYWORD,
                                                  regex=self.RESERVED_KEYWORD_REGEX)

    def get_top_level_keyword_token(self, input):
        '''
        Find token of type TokenType.TOP_LEVEL_KEYWORD in the query.

        Parameters
        input: string
            The query to format.
        
        Return: Token() object
            The identified top-level keyword token.
        '''
        return Tokenizer.get_token_on_first_match(input=input,
                                                  type=TokenType.TOP_LEVEL_KEYWORD,
                                                  regex=self.TOP_LEVEL_KEYWORD_REGEX)

    def get_newline_keyword_token(self, input):
        '''
        Find token of type TokenType.NEWLINE_KEYWORD in the query.

        Parameters
        input: string
            The query to format.
        
        Return: Token() object
            The identified newline keyword token.
        '''
        return Tokenizer.get_token_on_first_match(input=input,
                                                  type=TokenType.NEWLINE_KEYWORD,
                                                  regex=self.NEWLINE_KEYWORD_REGEX)

    def get_top_level_keyword_token_no_indent(self, input):
        '''
        Find token of type TokenType.TOP_LEVEL_KEYWORD_TOKEN_NO_INDENT in the query.

        Parameters
        input: string
            The query to format.
        
        Return: Token() object
            The identified token.
        '''
        return Tokenizer.get_token_on_first_match(input=input,
                                                  type=TokenType.TOP_LEVEL_KEYWORD_NO_INDENT,
                                                  regex=self.TOP_LEVEL_KEYWORD_NO_INDENT_REGEX)

    def get_plain_keyword_token(self, input):
        '''
        Find token of type TokenType.KEYWORD in the query.

        Parameters
        input: string
            The query to format.
        
        Return: Token() object
            The identified keyword token.
        '''
        return Tokenizer.get_token_on_first_match(input=input, type=TokenType.KEYWORD, regex=self.PLAIN_KEYWORD_REGEX)

    def get_word_token(self, input):
        '''
        Find token of type TokenType.WORD in the query.

        Parameters
        input: string
            The query to format.
        
        Return: Token() object
            The identified word token.
        '''
        return Tokenizer.get_token_on_first_match(input=input, type=TokenType.WORD, regex=self.WORD_REGEX)

    @staticmethod
    def get_token_on_first_match(input, type, regex):
        '''
        Find token of given type upon the first match.

        Parameters
        input: string
            The query to format.
        type: string
            Type of the token.
        regex: string
            The regex pattern that matches the token.
        
        Return: Token() object
            The matched token.
        '''
        if type in [
                TokenType.RESERVED_KEYWORD, TokenType.TOP_LEVEL_KEYWORD, TokenType.TOP_LEVEL_KEYWORD_NO_INDENT,
                TokenType.NEWLINE_KEYWORD, TokenType.KEYWORD, TokenType.OPEN_PAREN, TokenType.CLOSE_PAREN
        ]:
            # matches = re.search(pattern=regex, string=input, flags=re.IGNORECASE | re.UNICODE)
            matches = re.match(pattern=regex, string=input, flags=re.IGNORECASE | re.UNICODE)
        else:
            # matches = re.search(pattern=regex, string=input, flags=re.UNICODE)
            matches = re.match(pattern=regex, string=input, flags=re.UNICODE)
        if matches:
            return Token(type=type, value=matches.group(0))

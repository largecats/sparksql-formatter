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

from sparksqlformatter.src.tokenizer import TokenType, Tokenizer
from sparksqlformatter.src.indentation import Indentation
from sparksqlformatter.src.inline_block import InlineBlock
from sparksqlformatter.src.subquery import SubQuery
from sparksqlformatter.src.style import Style

trim_trailing_spaces = lambda s: re.sub(pattern='[ \t]+$', repl='', string=s)  # remove trailing spaces except \n


class Flag:
    '''
    Class for flags, or anotations, that can be added to tokens when formatting.
    '''
    SUBQUERY_ENDING_PAREN = 'SUBQUERY_ENDING_PAREN'
    INLINE = 'INLINE'  # don't add \n after comma in GROUP BY, ORDER BY, IN, etc


class Formatter:
    '''
    Class for formatting queries.
    '''
    def __init__(self, style=Style(), tokenOverride=None):
        '''
        Paramters
        style: sparksqlformatter.src.style.Style() object
            Styleurations for the query language.
        tokenOverride: function
            Function that takes token, previousKeyword and returns a token to overwrite given token (?).
        '''
        self.style = style
        self.indentation = Indentation(style.indent)
        self.inlineBlock = InlineBlock(style.inlineMaxLength)
        self.subQuery = SubQuery()
        self.tokenizer = Tokenizer(style=style)  # use the same styleurations as Formatter()
        self.tokenOverride = tokenOverride
        self.previousKeyword = None
        self.previousTopLevelKeyword = None
        self.tokens = []
        self.index = 0

    def format(self, query):
        '''
        Format query.
        
        Parameters
        query: str
            The query string.
        
        Return: str
            The formatted query.
        '''
        self.tokens = self.tokenizer.tokenize(input=query)  # identify tokens in the query
        formattedQuery = self.get_formatted_query_from_tokens()

        return formattedQuery.strip()

    def get_formatted_query_from_tokens(self):
        '''
        Create formatted query from identified tokens.

        Parameters

        Return: string
            The formatted query.
        '''
        formattedQuery = ''

        for i in range(len(self.tokens)):
            token = self.tokens[i]
            self.index = i

            if self.tokenOverride:
                token = self.tokenOverride(token, self.previousKeyword) or token

            if token.value.upper() == 'GROUP BY' or (token.value.upper() == 'ORDER BY'
                                                     and self.previousKeyword.value.upper() != 'PARTITION BY'):
                token.flag = Flag.INLINE

            # print("token.value = {}, token.type = {}".format(token.value, token.type))

            if token.type == TokenType.WHITESPACE:
                # ignore
                continue
            elif token.type == TokenType.LINE_COMMENT:
                formattedQuery = self.format_line_comment(token, formattedQuery)
            elif token.type == TokenType.BLOCK_COMMENT:
                formattedQuery = self.format_block_comment(token, formattedQuery)
            elif token.type == TokenType.TOP_LEVEL_KEYWORD_NO_INDENT:
                formattedQuery = self.format_top_level_keyword_no_indent(token, formattedQuery)
                self.previousKeyword = token
            elif token.type == TokenType.TOP_LEVEL_KEYWORD:
                formattedQuery = self.format_top_level_keyword(token, formattedQuery)
                self.previousKeyword = token
                self.previousTopLevelKeyword = token
            elif token.type == TokenType.NEWLINE_KEYWORD:
                formattedQuery = self.format_newline_keyword(token, formattedQuery)
                self.previousKeyword = token
            elif token.type == TokenType.RESERVED_KEYWORD:
                formattedQuery = self.format_with_spaces(token, formattedQuery)
                self.previousKeyword = token
            elif token.type == TokenType.KEYWORD:
                formattedQuery = self.format_with_spaces(token, formattedQuery)
                self.previousKeyword = token
            elif token.type == TokenType.OPEN_PAREN:
                formattedQuery = self.format_opening_parentheses(token, formattedQuery)
                if token.value == 'CASE':
                    self.previousKeyword = token
            elif token.type == TokenType.CLOSE_PAREN:
                formattedQuery = self.format_closing_parentheses(token, formattedQuery)
                if token.value == 'END':
                    self.previousKeyword = token
            elif token.value == ',':
                formattedQuery = self.format_comma(token, formattedQuery)
            elif token.value == ':':
                formattedQuery = Formatter.format_without_spaces_before_with_space_after(token, formattedQuery)
            elif token.value == '.':  # no space before or after
                formattedQuery = Formatter.format_without_spaces(token, formattedQuery)
            elif token.value == ';':
                formattedQuery = self.format_query_separator(token, formattedQuery)
            elif token.value == '-':
                if i > 1:
                    offset = 1
                    while self.previous_token(offset=offset).type == TokenType.WHITESPACE:
                        offset += 1  # find most immediate previous token that is not white space
                    if self.previous_token(offset=offset).type in [
                            TokenType.KEYWORD, TokenType.RESERVED_KEYWORD, TokenType.NEWLINE_KEYWORD,
                            TokenType.TOP_LEVEL_KEYWORD, TokenType.TOP_LEVEL_KEYWORD_NO_INDENT
                    ]:
                        formattedQuery = Formatter.format_without_spaces_after(token, formattedQuery)
                    else:
                        formattedQuery = self.format_with_spaces(token, formattedQuery)
            else:
                formattedQuery = self.format_with_spaces(token, formattedQuery)

        return formattedQuery

    def format_line_comment(self, token, query):
        '''
        Format line comment.

        Parameters
        token: sparksqlformatter.src.token.Token() object
            Identified token of type TOKEN.LINE_COMMENT.
        query: string
            The query formatted so far.
        
        Return: string
            The query formatted so far together with the newly formatted line comment.
        '''
        return self.add_newline(query.rstrip() + ' ' + token.value)

    def format_block_comment(self, token, query):
        '''
        Format block comment.

        Parameters
        token: sparksqlformatter.src.token.Token() object
            Identified token of type Token.BLOCK_COMMENT.
        query: string
            The query formatted so far.
        
        Return: string
            The query formatted so far together with the newly formatted block comment.
        '''
        return self.add_newline(self.add_newline(query) + self.indent_comment(token.value))

    def indent_comment(self, comment):
        '''
        Indent comment.

        Parameters
        comment: string
            Value of the comment token.
        
        Return: string
            The comment with proper indentation.
        '''
        return re.sub(pattern='\n[ \t]*', repl=('\n' + self.indentation.get_indent()), string=comment)

    def format_top_level_keyword_no_indent(self, token, query):
        '''
        Format top-level keywords that are not indented.

        Paramaters
        token: sparksqlformatter.src.token.Token() object
            Identified token of type Token.TOP_LEVEL_KEYWORD_NO_INDENT.
        query: string
            The query formatted so far.
        
        Return: string
            The query formatted so far together with the newly formatted top-level keyword with no indent.
        '''
        self.indentation.decrease_top_level()
        query = self.add_newline(query) + Formatter.equalize_white_space(self.format_reserved_keyword(token.value))
        return self.add_newline(query)

    def format_top_level_keyword(self, token, query):
        '''
        Format top-level keywords with indentation.

        Parameters
        token: sparksqlformatter.src.token.Token() object
            Identified token of type Token.TOP_LEVEL_KEYWORD.
        query: string
            The query formatted so far.
        
        Return: string
            The query formatted so far together with the newly formatted top-level keyword.
        '''
        self.indentation.decrease_top_level()
        query = self.add_newline(query)
        self.indentation.increase_top_level()
        query += Formatter.equalize_white_space(self.format_reserved_keyword(token.value))
        return self.add_newline(query)

    def format_newline_keyword(self, token, query):
        if (self.previousKeyword.value.upper() in ['BETWEEN'] and token.value.upper() in ['AND']):
            return query + Formatter.equalize_white_space(self.format_reserved_keyword(token.value)) + ' '
        else:
            return self.add_newline(query) + Formatter.equalize_white_space(self.format_reserved_keyword(
                token.value)) + ' '

    @staticmethod
    def equalize_white_space(s):
        '''
        Replace any sequence of whitespace characters with single space.

        Parameters
        s: string
            The string to process.
        
        Return: string
            The string s with all sequences of whitespace characters turned to single space.
        '''
        return re.sub(pattern='\s+', repl=' ', string=s)

    def format_opening_parentheses(self, token, query):
        '''
        Opening parentheses increase the block indent level and start a new line.
        Take out the preceding space unless there was whitespace there in the original query or another opening parens or line comment.

        Parameters
        token: sparksqlformatter.src.token.Token() object
            Identified token of type Token.OPEN_PAREN.
        query: string
            The query formatted so far.
        
        Return: string
            The query formatted so far together with the newly formatted opening parentheses.
        '''
        preserveWhiteSpaceFor = [TokenType.WHITESPACE, TokenType.OPEN_PAREN, TokenType.LINE_COMMENT]
        if not (any(t == self.previous_token().type for t in preserveWhiteSpaceFor)):
            query = trim_trailing_spaces(query)
        query += token.value.upper() if self.style.reservedKeywordUppercase else token.value.lower()

        # take care of block indent level
        self.inlineBlock.begin_if_possible(self.tokens, self.index)
        if not self.inlineBlock.is_active():
            self.indentation.increase_block_level()
            query = self.add_newline(query)

        # take care of subquery
        if token.value == '(':
            if (self.previousKeyword.value.upper() == 'AS' and
                (self.previous_token(offset=2).value.upper() == 'AS' or  # t0 AS (...)
                 (
                     self.previous_token(offset=1).type == TokenType.LINE_COMMENT  # t0 AS -- comment (...)
                     and self.previous_token(offset=3).value.upper() == 'AS'))):  # start of subQuery, e.g., t0 AS (...)
                # print("marking subquery start")
                self.subQuery.started = True  # mark that subquery has started
                # This is to differentiate from opening/closng parentheses inside subquery
                # and to distinguish the starting opening parenthesis of the subquery
            self.subQuery.update(self, token)  # update subquery with the current token

        return query

    def format_closing_parentheses(self, token, query):
        '''
        Closing parentheses decrease the block indent level.

        Parameters
        token: sparksqlformatter.src.token.Token() object
            Identified token of type Token.CLOSE_PAREN.
        query: string
            The query formatted so far.
        
        Return: string
            The query formatted so far together with the newly formatted closing parentheses.
        '''
        token.value = token.value.upper() if self.style.reservedKeywordUppercase else token.value.lower()

        # take care of block indent level
        if (self.inlineBlock.is_active()):
            self.inlineBlock.end()
            query = Formatter.format_without_spaces_before_with_space_after(token, query)
        else:
            self.indentation.decrease_block_level()
            query = self.format_with_spaces(token, self.add_newline(query))

        # take care of subquery
        if token.value == ')':  # if this is the subquery's ending closing parenthesis
            self.subQuery.update(self, token)  # update subquery with the current token
            if self.subQuery.started and self.subQuery.matched():
                token.flag = Flag.SUBQUERY_ENDING_PAREN  # add flag to mark this as subquery's ending parenthesis
                # print("Adding extra blank lines after subquery")
                query = query.rstrip() + '\n' * (1 + self.style.linesBetweenQueries)  # add extra blank lines
                self.subQuery.reset()  # reset to start again
        return query

    def format_comma(self, token, query):
        '''
        Commas start a new line (unless within inline parentheses or SQL "LIMIT" clause).

        Parameters
        token: sparksqlformatter.src.token.Token() object
            Identified token with value ','.
        query: string
            The query formatted so far.
        
        Return: string
            The query formatted so far together with the newly formatted comma.
        '''
        # if this is the comma immediately after the closing parenthesis of a subquery, add extra blank line
        if self.previous_token().flag == Flag.SUBQUERY_ENDING_PAREN:
            query = query.strip()  # remove the \n added immediately after )
            self.subQuery.reset()
            return query + token.value + '\n' * (1 + self.style.linesBetweenQueries)  # add \n after ),
        query = trim_trailing_spaces(query) + token.value + ' '
        if (self.inlineBlock.is_active()):
            return query
        if re.search(pattern='^LIMIT$', string=self.previousKeyword.value):
            return query
        if self.previousTopLevelKeyword.flag == Flag.INLINE:
            if self.style.splitOnComma:
                return self.add_newline(query)
            else:
                inlineLength = len(query) - query.rfind('\n') + 1
                if inlineLength < self.style.inlineMaxLength:  # if fit in a line, don't split at comma
                    return query
                else:  # else, split at comma
                    indent = self.indentation.get_indent()
                    lastCommaIndex = query.rfind(',')
                    query = query[:lastCommaIndex + 1] + '\n' + indent + query[lastCommaIndex +
                                                                               2:len(query)]  # split at the last comma
                    return query
        else:
            return self.add_newline(query)

    @staticmethod
    def format_without_spaces_before_with_space_after(token, query):
        '''
        Add token to formatted query, removing spaces before token and adding space after it.

        Parameters
        token: sparksqlformatter.src.token.Token() object
            Current token to be formatted.
        query: string
            The query formatted so far.
        
        Return: string
            The query formatted so far together with the newly formatted token.
        '''
        return trim_trailing_spaces(query) + token.value + ' '

    @staticmethod
    def format_without_spaces(token, query):
        '''
        Add token to formatted query, removing spaces before token without adding space after it.

        Parameters
        token: sparksqlformatter.src.token.Token() object
            Current token to be formatted.
        query: string
            The query formatted so far.
        
        Return: string
            The query formatted so far together with the newly formatted token.
        '''
        return trim_trailing_spaces(query) + token.value

    @staticmethod
    def format_without_spaces_after(token, query):
        '''
        Add token to formatted query with no space after it.

        Parameters
        token: sparksqlformatter.src.token.Token() object
            Current token to be formatted.
        query: string
            The query formatted so far.
        
        Return: string
            The query formatted so far together with the newly formatted token.
        '''
        return query + token.value

    def format_with_spaces(self, token, query):
        '''
        Add token to formatted query with space after it.

        Parameters
        token: sparksqlformatter.src.token.Token() object
            Current token to be formatted.
        query: string
            The query formatted so far.
        
        Return: string
            The query formatted so far together with the newly formatted token.
        '''
        if token.type == TokenType.RESERVED_KEYWORD:
            value = self.format_reserved_keyword(token.value)
        elif token.type == TokenType.KEYWORD:
            value = self.format_keyword(token.value)
        else:
            value = token.value
        return query + value + ' '

    def format_reserved_keyword(self, value):
        '''
        Format reserved keyword, converting to uppercase of lowercase depending on self.style.reservedKeywordUppercase.

        Parameters
        value: string
            Value of the Token.RESERVED_KEYWORD token.
        query: string
            The query formatted so far.
        
        Return: string
            The query formatted so far together with the newly formatted reserved keyword.
        '''
        return value.upper() if self.style.reservedKeywordUppercase else value.lower()

    def format_keyword(self, value):
        '''
        Format keyword.

        Parameters
        value: string
            Value of the Token.KEYWORD token.
        query: string
            The query formatted so far.
        
        Return: string
            The query formatted so far together with the newly formatted keyword.
        '''
        # return value.upper() if self.style.reservedKeywordUppercase else value.lower()
        return value

    def format_query_separator(self, token, query):
        '''
        Format ';', which separates queries, including blank lines between queries.

        Parameters
        token: sparksqlformatter.src.token.Token() object
            Identified token with value ';'.
        query: string
            The query formatted so far.
        
        Return: string
            The query formatted so far together with the newly formatted ';'.
        '''
        self.indentation.reset_indentation()
        return trim_trailing_spaces(query) + token.value + '\n' * (self.style.linesBetweenQueries or 1)

    def add_newline(self, query):
        '''
        Add blank line after the end of query with proper indentation.

        Parameters
        query: string
            The query to process.
        
        Return: string
            The query with newly added blank line and indentation.
        '''
        query = trim_trailing_spaces(query)
        if not query.endswith('\n'):
            query += '\n'
        return query + self.indentation.get_indent()

    def previous_token(self, offset=1):
        '''
        Get previous token.

        Parameters
        offset: int
            The number of tokens to trace back.

        Return: sparksqlformatter.src.token.Token() object or None
            The token obtained by stepping backwards by given offset, if it exists.
            Return None if there is no such token.
        '''
        return self.tokens[self.index - offset] or None

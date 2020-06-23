import re

class TokenType:
    WHITESPACE = 'whitespace'
    WORD = 'word'
    KEYWORD = 'keyword'
    STRING = 'string'
    RESERVED_KEYWORD = 'reserved-keyword'
    TOP_LEVEL_KEYWORD = 'top-level-keyword'
    TOP_LEVEL_KEYWORD_NO_INDENT = 'top-level-keyword-no-indent'
    NEWLINE_KEYWORD = 'newline-keyword'
    OPERATOR = 'operator'
    OPEN_PAREN = 'open-paren'
    CLOSE_PAREN = 'close-paren'
    LINE_COMMENT = 'line-comment'
    BLOCK_COMMENT = 'block-comment'
    NUMBER = 'number'

class Token:
    
    def __init__(self, type, value):
        __slots__ = 'type', 'value' # saves space since there would be many instances of Token
        self.type = type
        self.value = value

class Tokenizer:

    def __init__(self, config):
        self.WHITESPACE_REGEX = '^(\s+)'
        self.NUMBER_REGEX = '((-\s*)?[0-9]+(\.[0-9]+)?|0x[0-9a-fA-F]+|0b[01]+)\b'
        self.OPERATOR_REGEX = '^(!=|<>|==|<=|>=|!<|!>|\|\||::|->>|->|~~\*|~~|!~~\*|!~~|~\*|!~\*|!~|:=|.)'

        self.BLOCK_COMMENT_REGEX = '^(\/\*[.\\n]*?(?:\*\/|$))'
        self.LINE_COMMENT_REGEX = Tokenizer.create_line_comment_regex(config.lineCommentTypes)

        self.TOP_LEVEL_KEYWORD_REGEX = Tokenizer.create_keyword_regex(config.topLevelKeywords)
        self.TOP_LEVEL_KEYWORD_NO_INDENT_REGEX = Tokenizer.create_keyword_regex(config.topLevelKeywordsNoIndent)
        self.NEWLINE_KEYWORD_REGEX = Tokenizer.create_keyword_regex(config.newlineKeywords)
        self.PLAIN_KEYWORD_REGEX = Tokenizer.create_keyword_regex(config.keywords)

        self.WORD_REGEX = Tokenizer.create_word_regex(config.specialWordChars)
        self.STRING_REGEX = Tokenizer.create_string_regex(config.stringTypes)

        self.OPEN_PAREN_REGEX = Tokenizer.create_paren_regex(config.openParens)
        self.CLOSE_PAREN_REGEX = Tokenizer.create_paren_regex(config.closeParens)
    
    @staticmethod
    def create_line_comment_regex(lineCommentTypes):
        lineCommentTypesString = ('|').join(list(map(lambda c: re.escape(c), lineCommentTypes)))
        regexString = '^((?:{lineCommentTypesString}).*?(?:\r\n|\r|\n|$))'.format(lineCommentTypesString=lineCommentTypesString)
        return regexString
    
    @staticmethod
    def create_keyword_regex(keywords):
        keywordsString = ('|').join(keywords)
        keywordsPattern = re.sub(pattern=' ', repl='\\s+', string=keywordsString)
        regexString = '^({keywordsPattern})\\b'.format(keywordsPattern=keywordsPattern)
        return regexString
    
    @staticmethod
    def create_word_regex(specialChars=[]):
        specialCharsString = ('|').join(specialChars)
        regexString = u'^([\\w{specialCharsString}]+)'.format(specialCharsString=specialCharsString)
        return regexString
    
    @staticmethod
    def create_string_regex(stringTypes):
        regexString = '^(' + Tokenizer.create_string_pattern(stringTypes) + ')'
        return regexString

    @staticmethod
    def create_string_pattern(stringTypes):
        """
        This enables the following string patterns:
        1. backtick quoted string using `` to escape
        2. square bracket quoted string (SQL Server) using ]] to escape
        3. double quoted string using "" or \" to escape
        4. single quoted string using '' or \' to escape
        5. national character quoted string using N'' or N\' to escape
        """
        patterns = {
            '[]': '((\\[[^\\]]*($|\\]))(\\][^\\]]*($|\\]))*)',
            '""': '(("[^"\\\\]*(?:\\\\.[^"\\\\]*)*("|$))+)',
            "''": "(('[^'\\\\]*(?:\\\\.[^'\\\\]*)*('|$))+)",
            "N''": "((N'[^N'\\\\]*(?:\\\\.[^N'\\\\]*)*('|$))+)"
        }
        return ('|').join(list(map(lambda t: patterns[t], stringTypes)))
    
    @staticmethod
    def create_paren_regex(parens):
        parensString = ('|').join(list(map(lambda p: Tokenizer.escape_paren(p), parens)))
        return '^(' + parensString + ')'
    
    @staticmethod
    def escape_paren(paren):
        if (len(paren) == 1):
            return re.escape(paren)
        else:
            return '\\b' + paren + '\\b'
    
    def tokenize(self, input):
        """
        Takes a SQL string and breaks it into tokens.
        Each token is an object with type and value.
        """
        if not input:
            return []
        
        tokens = []
        token = None
        while len(input):
            print 'input = ' + input
            # Keep processing the string until it is empty
            token = self.get_next_token(input, token) # get next token
            print 'token.type = ' + token.type
            print 'token.value = ' + token.value
            start = 0 if token is None else len(token.value)
            print 'start = ' + str(start)
            input = input[start::] # advance thte string
            tokens.append(token)
        
        return tokens
    
    def get_next_token(self, input, previousToken):
        return (
            self.get_white_space_token(input) or
            self.get_comment_token(input) or
            self.get_string_token(input) or
            self.get_open_paren_token(input) or
            self.get_close_paren_token(input) or
            self.get_number_token(input) or
            self.get_keyword_token(input, previousToken) or
            self.get_word_token(input) or
            self.get_operator_token(input)
        )
    
    def get_white_space_token(self, input):
        return Tokenizer.get_token_on_first_match(
            input=input, 
            type=TokenType.WHITESPACE, 
            regex=self.WHITESPACE_REGEX
        )
    
    def get_comment_token(self, input):
        return self.get_line_comment_token(input) or self.get_block_comment_token(input)

    def get_line_comment_token(self, input):
        return Tokenizer.get_token_on_first_match(
            input=input,
            type=TokenType.LINE_COMMENT,
            regex=self.LINE_COMMENT_REGEX
        )
    
    def get_block_comment_token(self, input):
        return Tokenizer.get_token_on_first_match(
            input=input,
            type=TokenType.BLOCK_COMMENT,
            regex=self.BLOCK_COMMENT_REGEX
        )
    
    def get_string_token(self, input):
        return Tokenizer.get_token_on_first_match(
            input=input,
            type=TokenType.STRING,
            regex=self.STRING_REGEX
        )
    
    def get_open_paren_token(self, input):
        return Tokenizer.get_token_on_first_match(
            input=input,
            type=TokenType.OPEN_PAREN,
            regex=self.OPEN_PAREN_REGEX
        )
    
    def get_close_paren_token(self, input):
        return Tokenizer.get_token_on_first_match(
            input=input,
            type=TokenType.CLOSE_PAREN,
            regex=self.CLOSE_PAREN_REGEX
        )
    
    def get_number_token(self, input):
        return Tokenizer.get_token_on_first_match(
            input=input,
            type=TokenType.NUMBER,
            regex=self.NUMBER_REGEX
        )
    
    def get_operator_token(self, input):
        return Tokenizer.get_token_on_first_match(
            input=input,
            type=TokenType.OPERATOR,
            regex=self.OPERATOR_REGEX
        )
    
    def get_keyword_token(self, input, previousToken):
        """
        A keyword cannot be preceded by a "."
        This makes it so in "my_table.from", "from" is not considered a key word
        """
        if (previousToken and previousToken.value and previousToken.value == '.'):
            return
        return (
            self.get_top_level_keyword_token(input) or
            self.get_newline_keyword_token(input) or
            self.get_top_level_keyword_token_no_indent(input) or
            self.get_plain_keyword_token(input)
        )
    
    def get_top_level_keyword_token(self, input):
        return Tokenizer.get_token_on_first_match(
            input=input,
            type=TokenType.TOP_LEVEL_KEYWORD,
            regex=self.TOP_LEVEL_KEYWORD_REGEX
        )
    
    def get_newline_keyword_token(self, input):
        return Tokenizer.get_token_on_first_match(
            input=input,
            type=TokenType.TOP_LEVEL_KEYWORD,
            regex=self.NEWLINE_KEYWORD_REGEX
        )
    
    def get_top_level_keyword_token_no_indent(self, input):
        return Tokenizer.get_token_on_first_match(
            input=input,
            type=TokenType.TOP_LEVEL_KEYWORD_NO_INDENT,
            regex=self.TOP_LEVEL_KEYWORD_NO_INDENT_REGEX
        )
    
    def get_plain_keyword_token(self, input):
        return Tokenizer.get_token_on_first_match(
            input=input,
            type=TokenType.KEYWORD,
            regex=self.PLAIN_KEYWORD_REGEX
        )
    
    def get_word_token(self, input):
        return Tokenizer.get_token_on_first_match(
            input=input,
            type=TokenType.WORD,
            regex=self.WORD_REGEX
        )

    @staticmethod
    def get_token_on_first_match(input, type, regex):
        matches = re.search(pattern=regex, string=input)
        if matches:
            return Token(type=type, value=matches.group(0))

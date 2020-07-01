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
from __future__ import print_function # for print() in Python 2
import re

from hiveqlformatter.src.tokenizer import TokenType, Tokenizer
from hiveqlformatter.src.indentation import Indentation
from hiveqlformatter.src.inline_block import InlineBlock
from hiveqlformatter.src.subquery import SubQuery
from hiveqlformatter.src.config import Config

trim_trailing_spaces = lambda s: re.sub(pattern='[ \t]+$', repl='', string=s)

class Formatter:

    def __init__(self, config=Config(), tokenOverride=None):
        """
        Class for formatting queries.

        Paramters
        config: TBD
            config parser
        tokenizer: tokenizer.Tokenizer object
            TBD
        tokenOverrite: TBD
            TBD
        """
        self.config = config
        self.indentation = Indentation(config.indent)
        self.inlineBlock = InlineBlock()
        self.subQuery = SubQuery()
        self.tokenizer = Tokenizer(config=config)
        self.tokenOverride = tokenOverride
        self.previousKeyword = None
        self.tokens = []
        self.index = 0
    
    def format(self, query):
        """
        Formats whitespace in a query string.
        
        Parameters
        query: str
            The query string.
        
        Return: str
            The formatted query.
        """
        self.tokens = self.tokenizer.tokenize(input=query)
        formattedQuery = self.get_formatted_query_from_tokens()

        return formattedQuery.strip()

    def get_formatted_query_from_tokens(self):
        formattedQuery = ''

        for i in range(len(self.tokens)):
            # print('formattedQuery = \n')
            # print(formattedQuery)
            token = self.tokens[i]
            self.index = i

            if self.tokenOverride:
                token = self.tokenOverride(token, self.previousKeyword) or token
            
            # print('token.value = ' + token.value)
            # print('token.type = ' + token.type)
            if token.type == TokenType.WHITESPACE:
                # ignore
                continue
            elif token.type == TokenType.LINE_COMMENT:
                formattedQuery = self.format_line_comment(token, formattedQuery)
            elif token.type == TokenType.BLOCK_COMMENT:
                formattedQuery == self.format_block_comment(token, formattedQuery)
            elif token.type == TokenType.TOP_LEVEL_KEYWORD_NO_INDENT:
                formattedQuery = self.format_top_level_keyword_no_indent(token ,formattedQuery)
                self.previousKeyword = token
            elif token.type == TokenType.TOP_LEVEL_KEYWORD:
                formattedQuery = self.format_top_level_keyword(token, formattedQuery)
                self.previousKeyword = token
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
            elif token.type == TokenType.CLOSE_PAREN:
                formattedQuery = self.format_closing_parentheses(token, formattedQuery)
            elif token.value == ',':
                formattedQuery = self.format_comma(token, formattedQuery)
            elif token.value == ':':
                formattedQuery = Formatter.format_without_spaces_before_with_space_after(token, formattedQuery)
            elif token.value == '.':
                formattedQuery = Formatter.format_without_spaces(token, formattedQuery)
            elif token.value == ';':
                formattedQuery = self.format_query_separator(token, formattedQuery)
            elif token.value in ['{', '}']:
                if token.value == '{':
                    formattedQuery = Formatter.format_without_spaces_after(token, formattedQuery)
                else:
                    formattedQuery = Formatter.format_without_spaces_before_with_space_after(token, formattedQuery)
            elif token.value == '-':
                if i > 1 and self.tokens[i-1].type != TokenType.KEYWORD:
                    formattedQuery = Formatter.format_without_spaces_after(token, formattedQuery)
            else:
                formattedQuery = self.format_with_spaces(token, formattedQuery)
        
        return formattedQuery

    def format_line_comment(self, token, query):
        return self.add_newline(query + token.value)
    
    def format_block_comment(self, token ,query):
        return self.add_newline(self.add_newline(query) + self.indent_comment(token.value))

    def indent_comment(self, comment):
        return re.sub(pattern='\n[ \t]*', repl='\n', string=comment) + self.indentation.get_indent() + ' '
    
    def format_top_level_keyword_no_indent(self, token, query):
        self.indentation.decrease_top_level()
        query = self.add_newline(query) + Formatter.equalize_white_space(self.format_reserved_keyword(token.value))
        return self.add_newline(query)
    
    def format_top_level_keyword(self, token, query):
        self.indentation.decrease_top_level()
        query = self.add_newline(query)
        self.indentation.increase_top_level()
        query += Formatter.equalize_white_space(self.format_reserved_keyword(token.value))
        return self.add_newline(query)
    
    def format_newline_keyword(self, token, query):
        if (self.previousKeyword.value.upper() in ['BETWEEN', 'WHEN', 'ON'] 
            and token.value.upper() in ['AND', 'OR']):
            return query + Formatter.equalize_white_space(self.format_reserved_keyword(token.value)) + ' '
        else:
            return self.add_newline(query) + Formatter.equalize_white_space(self.format_reserved_keyword(token.value)) + ' '
    
    @staticmethod
    def equalize_white_space(s):
        """
        Replace any sequence of whitespace characters with single space.
        """
        return re.sub(pattern='\s+', repl=' ', string=s)
    
    def format_opening_parentheses(self, token, query):
        """
        Opening parentheses increase the block indent level and start a new line.
        Take out the preceding space unless there was whitespace there in the original query or another opening parens or line comment.
        """
        preserveWhiteSpaceFor = [
            TokenType.WHITESPACE,
            TokenType.OPEN_PAREN,
            TokenType.LINE_COMMENT
        ]
        if not (any(t == self.previous_token().type for t in preserveWhiteSpaceFor)):
            query = trim_trailing_spaces(query)
        query += token.value.upper() if self.config.reservedKeywordUppercase else token.value.lower()
        self.inlineBlock.begin_if_possible(self.tokens, self.index)
        if not self.inlineBlock.is_active():
            self.indentation.increase_block_level()
            query = self.add_newline(query)

        if self.previous_token(offset=2).value.upper() == 'AS': # start of subQuery, e.g., t0 AS (...)
            self.subQuery.reset() # reset so that occasional syntax error does not affect subsequent formatting
            self.subQuery.started = True # mark that subquery has started
            # This is to differentiate from opening/closng parentheses inside subquery
            # and to distinguish the starting opening parenthesis of the subquery
        self.subQuery.update(self, token) # update subquery with the current token
        
        return query
    
    def format_closing_parentheses(self, token, query):
        """
        Closing parentheses decrease the block indent level.
        """

        token.value = token.value.upper() if self.config.reservedKeywordUppercase else token.value.lower()
        if (self.inlineBlock.is_active()):
            self.inlineBlock.end()
            query = Formatter.format_without_spaces_before_with_space_after(token, query)
        else:
            self.indentation.decrease_block_level()
            query = self.format_with_spaces(token, self.add_newline(query))
        
        self.subQuery.update(self, token) # update subquery with the current token
        # print('self.subQuery.started = ' + str(self.subQuery.started))
        # print('self.subQuery.ended() = ' + str(self.subQuery.ended()))
        if self.subQuery.started and self.subQuery.ended(): # if this is the subquery's ending closing parenthesis
            query = query.rstrip() + '\n' * (1 + self.config.linesBetweenQueries) # add extra blank lines
            self.subQuery.reset() # mark subquery as ended to start again
        return query
    
    def format_comma(self, token, query):
        """
        Commas start a new line (unless within inline parentheses or SQL "LIMIT" clause)
        """
        if not self.subQuery.started and self.subQuery.ended(): # add extra blank line after subquery
            if self.previous_token().type == TokenType.CLOSE_PAREN:
                query = query.strip() # remove the \n added immediately after )
                return query + token.value + '\n' * (1 + self.config.linesBetweenQueries) # add \n after ),
        query = trim_trailing_spaces(query) + token.value + ' '
        if (self.inlineBlock.is_active()):
            return query
        elif re.search(pattern='^LIMIT$', string=self.previousKeyword.value):
            return query
        else:
            return self.add_newline(query)
    
    @staticmethod
    def format_without_spaces_before_with_space_after(token, query):
        return trim_trailing_spaces(query) + token.value + ' '
    
    @staticmethod
    def format_without_spaces(token, query):
        return trim_trailing_spaces(query) + token.value
    
    @staticmethod
    def format_without_spaces_after(token, query):
        return query + token.value

    def format_with_spaces(self, token, query):
        if token.type == TokenType.RESERVED_KEYWORD:
            value = self.format_reserved_keyword(token.value) 
        elif token.type == TokenType.KEYWORD:
            value = self.format_keyword(token.value)
        else:
            value = token.value
        return query + value + ' '
    
    def format_reserved_keyword(self, value):
        # print(value)
        # print(self.config.reservedKeywordUppercase)
        return value.upper() if self.config.reservedKeywordUppercase else value.lower()

    def format_keyword(self, value):
        # return value.upper() if self.config.reservedKeywordUppercase else value.lower()
        return value
    
    def format_query_separator(self, token, query):
        self.indentation.reset_indentation()
        return trim_trailing_spaces(query) + token.value + '\n' * (self.config.linesBetweenQueries or 1)
    
    def add_newline(self, query):
        query = trim_trailing_spaces(query)
        if not query.endswith('\n'):
            query += '\n'
        return query + self.indentation.get_indent()
    
    def previous_token(self, offset = 1):
        return self.tokens[self.index - offset] or None
    
    
    

        
    
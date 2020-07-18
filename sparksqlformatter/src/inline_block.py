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
from sparksqlformatter.src.tokenizer import TokenType


class InlineBlock:
    '''
    Class for managing inline blocks.

    Inline blocks are parenthesized expressions that are shorter than self.inlineMaxLength.
    These blocks are formatted on a single line, unlike longer parenthesized expressions where open-parenthesis causes newline and increase of indentation.
    '''
    def __init__(self, inlineMaxLength):
        self.level = 0
        self.inlineMaxLength = inlineMaxLength

    def begin_if_possible(self, tokens, index):
        """
        Begins inline block when lookahead through upcoming tokens determines that the block would be smaller than self.inlineMaxLength.

        Parameters
        tokens: list
            List of tokens.
        index: int
            Current token position.
        """
        if self.level == 0 and self.is_inline_block(tokens, index):
            self.level = 1
        elif self.level > 0:
            self.level += 1
        else:
            self.level = 0

    def end(self):
        """
        Finishes current inline block. There might be several nested ones.
        """
        self.level -= 1

    def is_active(self):
        """
        Check if currently is inside an inline block.

        Return: bool
            Returns True when inside an inline block.
        """
        return self.level > 0

    def is_inline_block(self, tokens, index):
        """
        Check if this should be an inline parentheses block.
        Examples are "NOW()", "COUNT(*)", "int(10)", key(`some_column`), DECIMAL(7,2).

        Parameters
        tokens: list
            List of tokens.
        index: int
            Current token position.
        """
        length = 0
        level = 0

        for i in range(index, len(tokens)):
            token = tokens[i]
            length += len(token.value)

            if length > self.inlineMaxLength:
                return False

            if token.type == TokenType.OPEN_PAREN:
                level += 1
            elif token.type == TokenType.CLOSE_PAREN:
                level -= 1
                if level == 0:
                    return True

            if InlineBlock.is_forbidden_token(token):
                return False

        return False

    @staticmethod
    def is_forbidden_token(token):
        '''
        Check if token does not belong to an inline block.

        Parameters
        token: sparksqlformatter.src.tokenizer.Token() object

        Return: bool
        '''
        type, value = token.type, token.value
        return (type == TokenType.TOP_LEVEL_KEYWORD or type == TokenType.NEWLINE_KEYWORD
                or type == TokenType.LINE_COMMENT or type == TokenType.BLOCK_COMMENT or value == ';')

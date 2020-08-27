# -*- coding: utf-8 -*-
# MIT License

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


class SubQuery:
    '''
    Class for maintaining the start and end of sub-queries.

    A sub-query is a query starting with
    WITH t0 AS (
        ...
    )
    or simply
    ...,
    t0 AS (
        ...
    )

    It needs to be succeeded by a comma if and only if the following statement is another sub-query. E.g.:

    WITH t0 AS (
        ...
    ),

    t1 AS (
        ...
    )

    SELECT * FROM t0
    '''
    def __init__(self):
        self.stack = []  # stack to hold unmatched opening and closing parentheses
        self.started = False  # whether a subquery has started, e.g., t0 AS (...)

    def matched(self):
        '''
        Check if all parentheses in the subquery have matched.

        Return: bool
        '''
        return len(self.stack) == 0

    def ended(self):
        '''
        Check if the subquery has ended.

        Return: bool
        '''
        return self.started and len(self.stack) == 0  # subQuery has started and parentheses are matched

    def update(self, formatter, token):
        '''
        Update self.stack and self.started with current token.

        Parameters
        formatter: sparksqlformatter.src.formatter.Formatter() object
            The formatter currently in use.
        token: sparksqlformatter.src.tokenizer.Token() object
            The current token.
        '''
        openParens = [p for p in formatter.style.openParens if p == '(']
        closeParens = [p for p in formatter.style.closeParens if p == ')']
        if token.value in openParens:  # push opening parenthesis onto stack
            self.stack.append(token.value)
        elif token.value in closeParens:
            if self.matched():  # no opening parenthesis to match
                raise Exception('Parentheses not matched')
            lastParen = self.stack[-1]  # retrieve last opening parenthesis
            if openParens.index(lastParen) == closeParens.index(token.value):  # check if they match
                self.stack.pop()  # remove the matched opening parenthesis
            else:
                raise Exception('Parentheses not matched')

    def reset(self):
        '''
        Reset the stack and started attributes of the class.
        '''
        self.started = False

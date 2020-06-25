# -*- coding: utf-8 -*-
'''
MIT License

Copyright (c) 2020-present largecats

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
'''
from src.common.tokenizer import TokenType

class SubQuery:
    
    def __init__(self):
        self.stack = []
    
    def is_ended(self):
        return len(self.stack) == 0
    
    def update(self, formatter, token):
        openParens = [p for p in formatter.config.openParens if p != 'CASE']
        closeParens = [p for p in formatter.config.closeParens if p != 'END']
        if token.value in openParens:
            self.stack.append(token.value)
        elif token.value in closeParens:
            if self.is_ended():
                raise Exception('Parentheses not matched')
            lastParen = self.stack[-1]
            if openParens.index(lastParen) == closeParens.index(token.value):
                self.stack.pop()
            else:
                raise Exception('Parentheses not matched')
    
    def reset(self):
        self.stack = []


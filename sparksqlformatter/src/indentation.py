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
INDENT_TYPE_TOP_LEVEL = 'top-level'  # increased by open parentheses
INDENT_TYPE_BLOCK_LEVEL = 'block-level'  # increased by TOPLEVEL_KEYWORD tokens


class Indentation:
    '''
    Class for managing indentation.
    '''
    def __init__(self, indent):
        '''
        Parameters
        indent: string
            One unit of indentation.
        '''
        self.indent = indent or '   '
        self.indentTypes = []  # store each indentation that needs to be applied

    def get_indent(self):
        """
        Get indentation at current level.

        Return: string
            The current level indentation.
        """
        return self.indent * len(self.indentTypes)

    def increase_top_level(self):
        """
        Increases indentation by one top-level indent.
        """
        self.indentTypes.append(INDENT_TYPE_TOP_LEVEL)

    def increase_block_level(self):
        """
        Increases indentation by one block-level indent.
        """
        self.indentTypes.append(INDENT_TYPE_BLOCK_LEVEL)

    def decrease_top_level(self):
        """
        Decreases indentation by one top-level indent.
        Does nothing if the previous indent is not top-level.
        """
        if len(self.indentTypes) > 0:
            if (self.indentTypes[-1] == INDENT_TYPE_TOP_LEVEL):
                self.indentTypes.pop()

    def decrease_block_level(self):
        """
        Decreases indentation by one block-level indent.
        If there are top-level indents within the block-level indent, throws away these as well.
        """
        while len(self.indentTypes) > 0:
            type = self.indentTypes.pop()
            if (type != INDENT_TYPE_TOP_LEVEL):
                break

    def reset_indentation(self):
        '''
        Reset indentation level by clearing self.indentTypes.
        '''
        self.indentTypes = []

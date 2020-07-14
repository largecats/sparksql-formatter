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
from sparksqlformatter.src import sparksql_config as sc


class Config:
    '''
    Class for configurations of the query language.
    '''
    def __init__(
            self,
            topLevelKeywords=sc.Keyword.TOP_LEVEL_KEYWORDS,
            topLevelKeywordsNoIndent=sc.Keyword.TOP_LEVEL_KEYWORDS_NO_INDENT,
            newlineKeywords=sc.Keyword.NEWLINE_KEYWORDS,
            stringTypes=['""', "''", '{}'],
            openParens=['(', 'CASE'],
            closeParens=[')', 'END'],  # the order of the parentheses need to match with openParens
            lineCommentTypes=['--'],
            reservedKeywordUppercase=True,
            linesBetweenQueries=1,
            specialWordChars=[],
            indent='    ',
            inlineMaxLength=120):
        '''
        Parameters
        topLevelKeywords: list
            Keywords that initiate top-level blocks in the query so that the following lines are indented.
            E.g., SELECT and FROM in
            SELECT
                ...
            FROM
                ...
        topLevelKeywordsNoIndent: list
            Keywords that initiate top-level blocks in the query without indenting the following lines.
            E.g., UNION in
            SELECT
                *
            FROM
                ...
            UNION
            SELECT
                *
            FROM
                ...
        newlineKeywords: list
            Keywords that initiate a newline in the query.
        stringTypes: list
            Pairs of characters that enclose strings in the query.
        openParens: list
            Characters tbat behave as opening parentheses in the query.
        closdParens: list
            Characters that behave as closing parentheses in the query. 
            The order of the closing parentheses need to match with that of the opening parentheses.
        lineCommentTypes: list
            Strings that initiate comments in the query.
        resercedKeywordsUppercase: bool
            If True, convert all reserved keywords to uppercase.
            Else, convert all reserved keywords to lowercase.
        linesBetweenQueries: int
            Number of blank lines to put between (sub)queries.
        specialWordChars: list
            Characters with special meanings in the query lanauge.
        indent: string
            One unit of indentation.
        inlineMaxLength: int
            Maximum length of an inline block.
        '''
        self.keywords = (sc.Keyword.RESERVED_KEYWORDS + sc.Keyword.NON_RESERVED_KEYWORDS +
                         sc.Function.AGGREGATE_FUNCTIONS + sc.Function.ARRAY_FUNCTIONS +
                         sc.Function.CONDITIONAL_FUNCTIONS + sc.Function.DATE_TIME_FUNCTIONS +
                         sc.Function.HASH_FUNCTIONS + sc.Function.JSON_FUNCTIONS + sc.Function.MAP_FUNCTIONS +
                         sc.Function.MATHEMATICAL_FUNCTIONS + sc.Function.MISC_FUNCTIONS +
                         sc.Function.OPERATOR_FUNCTIONS + sc.Function.STRING_FUNCTIONS + sc.Function.STRUCT_FUNCTIONS +
                         sc.Function.TABLE_GENERATING_FUNCTIONS + sc.Function.TYPE_CONVERSION_FUNCTIONS +
                         sc.Function.WINDOW_FUNCTIONS + sc.Function.XPATH_FUNCTIONS)
        self.reservedKeywords = sc.Keyword.RESERVED_KEYWORDS
        self.topLevelKeywords = topLevelKeywords
        self.newlineKeywords = newlineKeywords
        self.topLevelKeywordsNoIndent = topLevelKeywordsNoIndent
        self.stringTypes = stringTypes
        self.openParens = openParens
        self.closeParens = closeParens
        self.lineCommentTypes = lineCommentTypes
        self.reservedKeywordUppercase = reservedKeywordUppercase
        self.linesBetweenQueries = linesBetweenQueries
        self.specialWordChars = specialWordChars
        self.indent = indent
        self.inlineMaxLength = inlineMaxLength

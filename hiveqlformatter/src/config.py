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
from hiveqlformatter.src import hiveql_config as hc


class Config:
    '''
    Class for configurations of the query language.
    '''
    def __init__(
            self,
            keywords=(hc.Keywords.RESERVED_KEYWORDS + hc.Keywords.NON_RESERVED_KEYWORDS +
                      hc.Functions.MATHEMATICAL_FUNCTIONS + hc.Functions.COLLECTION_FUNCTIONS +
                      hc.Functions.TYPE_CONVERSION_FUNCTIONS + hc.Functions.DATE_FUNCTIONS +
                      hc.Functions.CONDITIONAL_FUNCTIONS + hc.Functions.STRING_FUNCTIONS +
                      hc.Functions.DATA_MASKING_FUNCTIONS + hc.Functions.MISC_FUNCTIONS +
                      hc.Functions.AGGREGATE_FUNCTIONS + hc.Functions.WINDOWING_FUNCTIONS +
                      hc.Functions.ANALYTICS_FUNCTIONS),
            reservedKeywords=hc.Keywords.RESERVED_KEYWORDS,
            topLevelKeywords=hc.Keywords.TOP_LEVEL_KEYWORDS,
            topLevelKeywordsNoIndent=hc.Keywords.TOP_LEVEL_KEYWORDS_NO_INDENT,
            newlineKeywords=hc.Keywords.NEWLINE_KEYWORDS,
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
        keywords: list
            Keywords in the query language.
        reservedKeywords: list
            Reserved keywords in the query language.
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
        self.keywords = keywords
        self.reservedKeywords = reservedKeywords
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

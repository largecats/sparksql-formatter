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
from sparksqlformatter.src import config

DEFAULT_STYLE_SECTION = 'sparksqlformatter'  # default section heading for style config files


class Style:
    '''
    Class for formatting style.
    '''
    def __init__(
            self,
            topLevelKeywords=config.Keyword.TOP_LEVEL_KEYWORDS,
            topLevelKeywordsNoIndent=config.Keyword.TOP_LEVEL_KEYWORDS_NO_INDENT,
            newlineKeywords=config.Keyword.NEWLINE_KEYWORDS,
            userDefinedFunctions=[],
            stringTypes=['""', "''", '{}', "``"],
            openParens=['(', '[', 'CASE'],
            closeParens=[')', ']', 'END'],  # the order of the parentheses need to match with openParens
            lineCommentTypes=['--'],
            reservedKeywordUppercase=True,
            linesBetweenQueries=1,
            specialWordChars=[],
            indent='    ',
            inlineMaxLength=120,
            splitOnComma=True):
        '''
        Parameters
        topLevelKeywords: list
            Keywords that initiate top-level blocks in the query so that the following lines are indented.
            E.g., SELECT and FROM in
            SELECT
                ...
            FROM
                ...
            Default to config.Keyword.TOP_LEVEL_KEYWORDS.
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
            Default to config.Keyword.TOP_LEVEL_KEYWORDS_NO_INDENT.
        newlineKeywords: list
            Keywords that initiate a newline in the query.
            Default to config.Keyword.NEWLINE_KEYWORDS.
        userDefinedFunctions: list
            Functions defined by user. To be treated as in-built functions in formatting.
            Default to [].
        stringTypes: list
            Pairs of characters that enclose strings in the query.
            Default to ['""', "''", '{}', '``'].
        openParens: list
            Characters tbat behave as opening parentheses in the query regarding block indent level.
            Default to ['(', '[', 'CASE']
        closdParens: list
            Characters that behave as closing parentheses in the query regarding block indent level. 
            The order of the closing parentheses need to match with that of the opening parentheses.
            Default to [')', ']', 'END']
        lineCommentTypes: list
            Strings that initiate comments in the query.
            Default to ['--']
        resercedKeywordsUppercase: bool
            If True, convert all reserved keywords to uppercase.
            Else, convert all reserved keywords to lowercase.
            Default to True.
        linesBetweenQueries: int
            Number of blank lines to put between (sub)queries.
            Default to 1.
        specialWordChars: list
            Characters with special meanings in the query lanauge.
            Default to [].
        indent: string
            One unit of indentation.
            Default to '    '.
        inlineMaxLength: int
            Maximum length of an inline block.
            Default to 120.
        splitOnComma: bool
           If true, in cases where a comma separated list in GROUP BY, ORDER BY clauses is too long to fit in a line, split such that all elements are on a single line.
           Else, will only split at inlineMaxLength.
           Default to True.
        # '''
        # self.keywords = (config.Keyword.RESERVED_KEYWORDS + config.Keyword.NON_RESERVED_KEYWORDS +
        #                  config.Function.AGGREGATE_FUNCTIONS + config.Function.ARRAY_FUNCTIONS +
        #                  config.Function.CONDITIONAL_FUNCTIONS + config.Function.DATE_TIME_FUNCTIONS +
        #                  config.Function.HASH_FUNCTIONS + config.Function.JSON_FUNCTIONS + config.Function.MAP_FUNCTIONS +
        #                  config.Function.MATHEMATICAL_FUNCTIONS + config.Function.MISC_FUNCTIONS +
        #                  config.Function.OPERATOR_FUNCTIONS + config.Function.STRING_FUNCTIONS + config.Function.STRUCT_FUNCTIONS +
        #                  config.Function.TABLE_GENERATING_FUNCTIONS + config.Function.TYPE_CONVERSION_FUNCTIONS +
        #                  config.Function.WINDOW_FUNCTIONS + config.Function.XPATH_FUNCTIONS + userDefinedFunctions)
        # self.reservedKeywords = config.Keyword.RESERVED_KEYWORDS
        self.topLevelKeywords = topLevelKeywords
        self.newlineKeywords = newlineKeywords
        self.topLevelKeywordsNoIndent = topLevelKeywordsNoIndent
        self.userDefinedFunctions = userDefinedFunctions
        self.stringTypes = stringTypes
        self.openParens = openParens
        self.closeParens = closeParens
        self.lineCommentTypes = lineCommentTypes
        self.reservedKeywordUppercase = reservedKeywordUppercase
        self.linesBetweenQueries = linesBetweenQueries
        self.specialWordChars = specialWordChars
        self.indent = indent
        self.inlineMaxLength = inlineMaxLength
        self.splitOnComma = splitOnComma

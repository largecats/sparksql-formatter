# -*- coding: utf-8 -*-
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from hqlf.src.languages import hiveql_config as hc
from hqlf.src.core.tokenizer import Tokenizer
from hqlf.src.core.formatter import Formatter
from hqlf.src.core.config import Config

class HiveQlFormatter:

    def __init__(self, config=None):
        self.config = config or \
            Config(
                keywords=(
                    hc.Keywords.RESERVED_KEYWORDS + hc.Keywords.NON_RESERVED_KEYWORDS + 
                    hc.Functions.MATHEMATICAL_FUNCTIONS +
                    hc.Functions.COLLECTION_FUNCTIONS +
                    hc.Functions.TYPE_CONVERSION_FUNCTIONS + 
                    hc.Functions.DATE_FUNCTIONS + 
                    hc.Functions.CONDITIONAL_FUNCTIONS + 
                    hc.Functions.STRING_FUNCTIONS +
                    hc.Functions.DATA_MASKING_FUNCTIONS +
                    hc.Functions.MISC_FUNCTIONS +
                    hc.Functions.AGGREGATE_FUNCTIONS +
                    hc.Functions.WINDOWING_FUNCTIONS +
                    hc.Functions.ANALYTICS_FUNCTIONS
                ),
                reservedKeywords=hc.Keywords.RESERVED_KEYWORDS,
                topLevelKeywords=hc.Keywords.TOP_LEVEL_KEYWORDS,
                topLevelKeywordsNoIndent=hc.Keywords.TOP_LEVEL_KEYWORDS_NO_INDENT,
                newlineKeywords=hc.Keywords.NEWLINE_KEYWORDS,
                stringTypes=['""', "N''", "''", '[]'],
                openParens=['(', 'CASE'], # the order of the parentheses need to match with closeParens
                closeParens=[')', 'END'],
                lineCommentTypes=['--'],
                reservedKeywordUppercase=True,
                linesBetweenQueries=1,
                specialWordChars=[],
                indent='    '
            )
    
    def format(self, query):
        tokenizer = Tokenizer(config=self.config)
        return Formatter(config=self.config, tokenizer=tokenizer, tokenOverride=None).format(query)
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from src import hiveql_config as hc
from src.common.tokenizer import Tokenizer
from src.common.formatter import Formatter
from src.common.config import Config

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
                newlineKeywords=hc.Keywords.NEWLINE_KEYWORDS,
                topLevelKeywordsNoIndent=hc.Keywords.TOP_LEVEL_KEYWORDS_NO_INDENT,
                stringTypes=['""', "N''", "''", '[]'],
                openParens=['(', 'CASE'],
                closeParens=[')', 'END'],
                lineCommentTypes=['--'],
                keywordUppercase=True,
                linesBetweenQueries=1,
                specialWordChars=[],
                indent='    '
            )
    
    def format(self, query):
        tokenizer = Tokenizer(config=self.config)
        return Formatter(config=self.config, tokenizer=tokenizer, tokenOverride=None).format(query)
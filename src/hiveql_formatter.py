import hiveql_config as hc
from common.tokenizer import Tokenizer
from common.formatter import Formatter
from common.config import Config

class HiveQlFormatter:

    def __init__(self, config=None):
        self.config = config or \
            Config(
                keywords=(
                    hc.Keywords.RESERVED_KEYWORDS + hc.Keywords.NON_RESERVED_KEYWORDS + 
                    list(map(lambda s: s.upper(), hc.Functions.MATHEMATICAL_FUNCTIONS)) +
                    list(map(lambda s: s.upper(), hc.Functions.COLLECTION_FUNCTIONS)) +
                    list(map(lambda s: s.upper(), hc.Functions.TYPE_CONVERSION_FUNCTIONS)) + 
                    list(map(lambda s: s.upper(), hc.Functions.DATE_FUNCTIONS)) + 
                    list(map(lambda s: s.upper(), hc.Functions.CONDITIONAL_FUNCTIONS)) + 
                    list(map(lambda s: s.upper(), hc.Functions.STRING_FUNCTIONS)) +
                    list(map(lambda s: s.upper(), hc.Functions.DATA_MASKING_FUNCTIONS)) +
                    list(map(lambda s: s.upper(), hc.Functions.MISC_FUNCTIONS)) +
                    list(map(lambda s: s.upper(), hc.Functions.AGGREGATE_FUNCTIONS)) +
                    list(map(lambda s: s.upper(), hc.Functions.WINDOWING_FUNCTIONS)) +
                    list(map(lambda s: s.upper(), hc.Functions.ANALYTICS_FUNCTIONS))
                ),
                topLevelKeywords=hc.Keywords.TOP_LEVEL_KEYWORDS,
                newlineKeywords=hc.Keywords.NEWLINE_KEYWORDS,
                topLevelKeywordsNoIndent=hc.Keywords.TOP_LEVEL_KEYWORDS_NO_INDENT,
                stringTypes=[`""`, "N''", "''", '[]'],
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
# -*- coding: utf-8 -*-
from __future__ import print_function # for print() in Python 2
import os
import sys
import argparse
import logging
import codecs

from hqlf.src.languages.hiveql_formatter import HiveQlFormatter
from hqlf.src.languages import hiveql_config as hc
from hqlf.src.core.config import Config

logger = logging.getLogger(__name__)
log_formatter = '[%(asctime)s] %(levelname)s [%(filename)s:%(lineno)s:%(funcName)s] %(message)s'
logging.basicConfig(stream=sys.stdout, level=logging.INFO, format=log_formatter)
logger.info('Script loaded...')

def main(argv):
    args = get_arguments(argv)
    config = Config(
                keywords=args['keywords'],
                reservedKeywords=args['reservedKeywords'],
                topLevelKeywords=args['topLevelKeywords'],
                topLevelKeywordsNoIndent=args['topLevelKeywordsNoIndent'],
                newlineKeywords=args['newlineKeywords'],
                stringTypes=args['stringTypes'],
                openParens=args['openParens'],
                closeParens=args['closeParens'],
                lineCommentTypes=args['lineCommentTypes'],
                reservedKeywordUppercase=args.get('reservedKeywordUppercase') or False,
                linesBetweenQueries=args['linesBetweenQueries'],
                specialWordChars=args['specialWordChars'],
                indent=args['indent']
            )
    formatter = HiveQlFormatter(config=config)
    filenames = args['files']
    for filename in filenames:
        format_file(formatter, filename, args.get('in_place'))

def format_file(formatter, filename, in_place=False):
    query = read_from_file(filename)
    reformattedQuery = formatter.format(query)
    if in_place: # overwrite file
        logger.info('Writing to ' + filename + '...')
        write_to_file(reformattedQuery, filename)
    else: # write to stdout
        sys.stdout.write(reformattedQuery)

def read_from_file(filename):
    with codecs.open(filename=filename, mode='r', encoding='utf-8') as f:
        text = f.read()
    return text

def write_to_file(reformattedQuery, filename):
    with codecs.open(filename=filename, mode='w', encoding='utf-8') as f:
        f.write(reformattedQuery)

def get_arguments(argv):
    '''
    Return arguments passed via command-line.

    Paramters:
    argv: list
        sys.argv
    
    Returns: dict
        A dictionary containing arguments for the formatter.
    '''
    parser = argparse.ArgumentParser(description='Formatter parameters')

    parser.add_argument(
        '-files',
        type=str, 
        nargs='+',
        help='Files to format'
    )

    parser.add_argument(
        '-i',
        '--in-place',
        action='store_true',
        help='Format the files in place'
    )

    parser.add_argument(
        '-keywords', 
        type=list, 
        default=(
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
        help='Keywords in the query language')

    parser.add_argument(
        '-reservedKeywords', 
        type=list, 
        default=hc.Keywords.RESERVED_KEYWORDS,
        help='Reserved keywords in the query language')

    parser.add_argument(
        '-topLevelKeywords', 
        type=list, 
        default=hc.Keywords.TOP_LEVEL_KEYWORDS,
        help='Keywords in the query language that initiate a block indent')

    parser.add_argument(
        '-topLevelKeywordsNoIndent', 
        type=list, 
        default=hc.Keywords.TOP_LEVEL_KEYWORDS_NO_INDENT,
        help='Keywords in the query language that initiate a block without indent')

    parser.add_argument(
        '-newlineKeywords', 
        type=list, 
        default=hc.Keywords.NEWLINE_KEYWORDS,
        help='Keywords in the query language that initiate a newline character')

    parser.add_argument(
        '-stringTypes', 
        type=list, 
        default=['""', "N''", "''", '[]'],
        help='Types of strings in the query language')

    parser.add_argument(
        '-openParens', 
        type=list, 
        default=['(', 'CASE'],
        help='Opening parentheses in the query language')

    parser.add_argument(
        '-closeParens', 
        type=list, 
        default=[')', 'END'],
        help='Closing parentheses in the query language')

    parser.add_argument(
        '-lineCommentTypes', 
        type=list, 
        default=['--'],
        help='Prefixes to line comments in the query language')

    parser.add_argument(
        '-u',
        '-reservedKeywordUppercase', 
        action='store_true',
        help='Convert the reserved keywords to upper case')

    parser.add_argument(
        '-linesBetweenQueries', 
        type=int, 
        default=1,
        help='Number of blank lines to insert between adjacent queries')

    parser.add_argument(
        '-specialWordChars', 
        type=list, 
        default=[],
        help='Characters with special meaning in the query language')

    parser.add_argument(
        '-indent', 
        type=str, 
        default='    ',
        help='One unit of indent')
    
    args = vars(parser.parse_args(argv[1:]))

    return args


if __name__ == '__main__':
    main(sys.argv)
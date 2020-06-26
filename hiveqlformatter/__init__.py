# -*- coding: utf-8 -*-
from __future__ import print_function # for print() in Python 2
import os
import sys
import argparse
import configparser
import logging
import codecs
import json
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from hiveqlformatter.src.languages.hiveql_formatter import HiveQlFormatter
from hiveqlformatter.src.languages import hiveql_config as hc
from hiveqlformatter.src.core.config import Config

logger = logging.getLogger(__name__)
log_formatter = '[%(asctime)s] %(levelname)s [%(filename)s:%(lineno)s:%(funcName)s] %(message)s'
logging.basicConfig(stream=sys.stdout, level=logging.INFO, format=log_formatter)

DEFAULT_CONFIG_SECTION = 'hiveql-formatter'

def main(argv):
    args = get_arguments(argv)
    config = Config(
                keywords=args.get('keywords') or (
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
                reservedKeywords=args.get('reservedKeywords') or hc.Keywords.RESERVED_KEYWORDS,
                topLevelKeywords=args.get('topLevelKeywords') or hc.Keywords.TOP_LEVEL_KEYWORDS,
                topLevelKeywordsNoIndent=args.get('topLevelKeywordsNoIndent') or hc.Keywords.TOP_LEVEL_KEYWORDS_NO_INDENT,
                newlineKeywords=args.get('newlineKeywords') or hc.Keywords.NEWLINE_KEYWORDS,
                stringTypes=args.get('stringTypes') or ['""', "N''", "''", '[]'],
                openParens=args.get('openParens') or ['(', 'CASE'],
                closeParens=args.get('closeParens') or [')', 'END'],
                lineCommentTypes=args.get('lineCommentTypes') or ['--'],
                reservedKeywordUppercase= True if args.get('reservedKeywordUppercase') is None else args.get('reservedKeywordUppercase'),
                linesBetweenQueries=args.get('linesBetweenQueries') or 1,
                specialWordChars=args.get('specialWordChars') or [],
                indent=args.get('indent') or '    '
            )
    formatter = HiveQlFormatter(config=config)
    filenames = args['files']
    if filenames:
        for filename in filenames:
            format_file(formatter, filename, args.get('in_place'))

def convert_to_bool(s):
    if s:
        return s.upper() == 'TRUE'

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
    parser = argparse.ArgumentParser(description='hiveql-formatter parameters')

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
        '--config',
        type=str,
        default=None,
        help="Configurations for the query language. Can be a path to a config file or a dictionary."
    )
    
    args = vars(parser.parse_args(argv[1:]))
    config = args['config']
    if config:
        configParser = configparser.ConfigParser()
        configParser.optionxform = str # makes the parser case-sensitive
        if config.startswith('{'):
            configWithHeader = {DEFAULT_CONFIG_SECTION: eval(config)}
            configParser.read_dict(configWithHeader)
            for key in configParser[DEFAULT_CONFIG_SECTION]:
                if key == 'reservedKeywordUppercase':
                    args[key] = configParser.getboolean(DEFAULT_CONFIG_SECTION, key) == 'True'
                else:
                    args[key] = configParser[DEFAULT_CONFIG_SECTION][key]
        else:
            configParser.read(config)
            if DEFAULT_CONFIG_SECTION in configParser:
                for key in configParser[DEFAULT_CONFIG_SECTION]:
                    args[key] = configParser[DEFAULT_CONFIG_SECTION][key]

    return args

def run_main():
    main(sys.argv)

if __name__ == '__main__':
    run_main()
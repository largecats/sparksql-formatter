# -*- coding: utf-8 -*-
# MIT License

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
from __future__ import print_function # for print() in Python 2
import os
import sys
import argparse
import configparser
import logging
import codecs
import json
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from hiveqlformatter.src.languages.hiveql_formatter import HiveqlFormatter
from hiveqlformatter.src.languages import hiveql_config as hc
from hiveqlformatter.src.core.config import Config
from hiveqlformatter.src.core import api

logger = logging.getLogger(__name__)
log_formatter = '[%(asctime)s] %(levelname)s [%(filename)s:%(lineno)s:%(funcName)s] %(message)s'
logging.basicConfig(stream=sys.stdout, level=logging.INFO, format=log_formatter)

def main(argv):
    args = get_arguments(argv)
    configParam = args['config']
    if configParam:
        if configParam.startswith('{'): # config is passed as dictionary
            config = api.create_config_from_dict(eval(configParam))
        else: # config is passed as file
            config = api.create_config_from_file(configParam)
        formatter = HiveqlFormatter(config)
    else:
        formatter = HiveqlFormatter()
    filenames = args['files']
    if filenames:
        for filename in filenames:
            api.format_file(filename, formatter, args.get('inplace'))

def convert_to_bool(s):
    if s:
        return s.upper() == 'TRUE'

def get_arguments(argv):
    '''
    Return arguments passed via command-line.

    Paramters:
    argv: list
        sys.argv
    
    Returns: dict
        A dictionary containing arguments for the formatter.
    '''
    parser = argparse.ArgumentParser(description='Formatter for HiveQL queries.')

    parser.add_argument(
        '-files',
        type=str, 
        nargs='+',
        help='Paths to files to format.'
    )

    parser.add_argument(
        '-i',
        '--inplace',
        action='store_true',
        help='Format the files in place.'
    )

    parser.add_argument(
        '--config',
        type=str,
        default=None,
        help="Configurations for the query language. Can be a path to a config file or a dictionary."
    )
    
    args = vars(parser.parse_args(argv[1:]))

    return args

def run_main():
    main(sys.argv)

if __name__ == '__main__':
    run_main()
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
# from __future__ import print_function  # for print() in Python 2
import os
import sys
import argparse
import logging
import codecs
import json
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from sparksqlformatter.src.style import Style
from sparksqlformatter.src import api
from sparksqlformatter.src.formatter import Formatter

logger = logging.getLogger(__name__)
log_formatter = '[%(asctime)s] %(levelname)s [%(filename)s:%(lineno)s:%(funcName)s] %(message)s'
logging.basicConfig(stream=sys.stdout, level=logging.INFO, format=log_formatter)


def main(argv):
    '''
    Main function that enables formatting file from command-line.

    Parameters
    argv: list
        List of arguments in sys.argv, excluding the first argument which is the script itself.
    '''
    args = get_arguments(argv)
    style = args['style']
    filePaths = args['files']
    if filePaths:
        if style:
            for filePath in filePaths:
                api.format_file(filePath=filePath, style=style, inPlace=args.get('in_place'))
        else:
            for filePath in filePaths:
                api.format_file(filePath=filePath, inPlace=args.get('in_place'))


def get_arguments(argv):
    '''
    Get arguments passed via command-line in dictionary.

    Paramters:
    argv: list
        List of arguments in sys.argv, including the first argument which is the script itself.
    
    Returns: dict
        A dictionary containing arguments for the formatter.
    '''
    parser = argparse.ArgumentParser(description='Formatter for SparkSQL queries.')

    parser.add_argument('-f', '--files', type=str, nargs='+', help='Paths to files to format.')

    parser.add_argument('-i', '--in-place', action='store_true', help='Format the files in place.')

    parser.add_argument('--style',
                        type=str,
                        default=None,
                        help="Style configurations for SparkSQL. Can be a path to a style config file or a dictionary.")

    args = vars(parser.parse_args(argv[1:]))

    return args


def run_main():
    '''
    Entry point for console_scripts in setup.py
    '''
    main(sys.argv)


if __name__ == '__main__':
    run_main()

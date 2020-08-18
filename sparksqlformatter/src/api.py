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
from io import open  # for open() in Python 2
import sys
import re
import logging
if sys.version_info[0] >= 3:
    import configparser
else:
    from backports import configparser
import ast

from sparksqlformatter.src.style import Style
from sparksqlformatter.src.formatter import Formatter
from sparksqlformatter.src.style import DEFAULT_STYLE_SECTION

logger = logging.getLogger(__name__)
log_formatter = '[%(asctime)s] %(levelname)s [%(filename)s:%(lineno)s:%(funcName)s] %(message)s'
logging.basicConfig(stream=sys.stdout, level=logging.INFO, format=log_formatter)


def format_file(filePath, style=Style(), inPlace=False):
    '''
    Format given file with given styleurations.

    Parameters
    filePath: string
        Path to the file to format.
    style: string, dict, or sparksqlformatter.src.style.Style() object
        Styleurations for the query language.
    inPlace: bool
        If True, will format the file in place.
        Else, will write the formatted file to stdout.
    '''
    if type(style) == type(Style()):  # style is a Style() object
        formatter = Formatter(style=style)
    else:  # create Style() object from style
        if type(style) == str:
            if style.startswith('{'):  # style is a dictionary in string
                style = eval(style)
                formatter = Formatter(style=_create_style_from_dict(style))
            else:  # style is a file path
                formatter = Formatter(style=_create_style_from_file(style))
        elif type(style) == dict:  # style is a dictionary
            formatter = Formatter(style=_create_style_from_dict(style))
        else:
            raise Exception('Unsupported style type')
    _format_file(filePath, formatter, inPlace)


def format_query(query, style=Style()):
    '''
    Format query using given styleurations.

    Parameters
    query: string
        The query to be formatted.
    style: string, dict, or sparksqlformatter.src.style.Style() object
        Styleurations for the query language.
    
    Return: string
        The formatted query.
    '''
    if type(style) == type(Style()):
        formatter = Formatter(style=style)
    else:
        if type(style) == str:
            if style.startswith('{'):
                style = eval(style)
                formatter = Formatter(style=_create_style_from_dict(style))
            else:
                formatter = Formatter(style=_create_style_from_file(style))
        elif type(style) == dict:
            formatter = Formatter(style=_create_style_from_dict(style))
        else:
            raise Exception('Unsupported style type')
    return _format_query(query, formatter)


def _format_file(filePath, formatter, inPlace=False):
    '''
    The I/O helper function for format_file(). Read from given file, format it, and write to specified output.

    Parameters
    filePath: string
        Path to the file to format.
    formatter: sparksqlformatter.src.formatter.Formatter() object
        Formatter.
    inPlace: bool
        If True, will format the file in place.
        Else, will write the formatted file to stdout.
    '''
    query = _read_from_file(filePath)
    formattedQuery = _format_query(query, formatter)
    if inPlace:  # overwrite file
        logger.info('Writing to ' + filePath + '...')
        _write_to_file(formattedQuery, filePath)
    else:  # write to stdout
        sys.stdout.write(formattedQuery)


def _read_from_file(filePath):
    '''
    The input helper function for _format_file(). Read from given file and return its content.

    Parameters
    filePath: string
        Path to the file to format.
    
    Return: string
        The file content.
    '''
    # see https://docs.python.org/3.5/library/functions.html#open
    with open(file=filePath, mode='r', newline=None, encoding='utf-8') as f:
        text = f.read()
    return text


def _write_to_file(formattedQuery, filePath):
    '''
    The output helper function for _format_file(). Write formatted query to given file.

    Parameters
    formattedQuery: string
        The formatted query.
    filePath: string
        Path to the file to write to.
    '''
    # see https://docs.python.org/3.5/library/functions.html#open
    with open(file=filePath, mode='w', newline='\n', encoding='utf-8') as f:
        f.write(formattedQuery)


def _format_query(query, formatter):
    '''
    The wrapper function for format_query(). Format a given query using given formatter.

    Parameters
    query: string
        The query to format.
    formatter: sparksqlformatter.src.formatter.Formatter object
        Formatter.
    
    Return: string
        The formatted query
    '''
    return formatter.format(query)


def _create_style_from_dict(styleDict, defaultStyleSection=DEFAULT_STYLE_SECTION):
    '''
    Create Style() object from dictionary.

    Parameters
    styleDict: dict
        A dictionary of styleurations specified in key-value pairs.
    defaultStyleSection: string
        The top-level style section that needs to be added on top of the styleDict before feeding to styleParser.read_dict(), default to 'sparksqlformatter'.
    
    Return: sparksqlformatter.src.style.Style() object
        The Style() object created from styleDict.
    '''
    styleParser = configparser.ConfigParser()
    styleParser.optionxform = str  # makes the parser case-sensitive
    if defaultStyleSection not in styleDict:
        styleDict = {defaultStyleSection: styleDict}  # add top-level section
    styleParser.read_dict(styleDict)  # styleParser assumes the existence of a top-level section
    args = _parse_args_in_correct_type(styleParser, defaultStyleSection)
    style = Style(**args)
    return style


def _create_style_from_file(styleFilePath, defaultStyleSection=DEFAULT_STYLE_SECTION):
    '''
    Create Style() object from style file.

    Parameters
    styleFilePath: string
        Path to the style file.
    defaultStyleSection: string
        The top-level style section that needs to be added on top of the styleDict before feeding to styleParser.read_dict(), default to 'sparksqlformatter'.
    
    Return: sparksqlformatter.src.style.Style() object
        The Style() object created from the style file.
    '''
    styleParser = configparser.ConfigParser()
    styleParser.optionxform = str  # makes the parser case-sensitive
    styleParser.read(styleFilePath)
    if defaultStyleSection in styleParser:
        styleDict = _parse_args_in_correct_type(styleParser, defaultStyleSection)
        return Style(**styleDict)
    else:
        raise Exception('Section ' + defaultStyleSection + 'not found in ' + styleFilePath)


def _parse_args_in_correct_type(styleParser, defaultStyleSection=DEFAULT_STYLE_SECTION):
    '''
    Parse paramters in style with special handling to convert boolean values converted from string back to boolean type.

    Parameters
    styleParser: a styleParser.ConfigParser() object
        Parser for style files.
    defaultStyleSection: string
        The top-level style section that needs to be added on top of the styleDict before feeding to styleParser.read_dict(), default to 'sparksqlformatter'.
    
    Return: dict
        A dictionary of styleuration key-value pairs where values are of correct type.
    '''
    args = {}
    for key in styleParser[defaultStyleSection]:
        args[key] = ast.literal_eval(styleParser[defaultStyleSection][key])
    return args

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
import sys
import re
import codecs
import logging
import configparser
import ast

from hiveqlformatter.src.config import Config
from hiveqlformatter.src.formatter import Formatter
from hiveqlformatter.src.hiveql_config import DEFAULT_CONFIG_SECTION

logger = logging.getLogger(__name__)
log_formatter = '[%(asctime)s] %(levelname)s [%(filename)s:%(lineno)s:%(funcName)s] %(message)s'
logging.basicConfig(stream=sys.stdout, level=logging.INFO, format=log_formatter)

def format_file(filename, config=Config(), inplace=False):
    if type(config) == type(Config()):
        formatter = Formatter(config=config)
    else:
        if type(config) == str:
            if config.startswith('{'):
                config = eval(config)
                formatter = Formatter(config=_create_config_from_dict(config))
            else:
                formatter = Formatter(config=_create_config_from_file(config))
        elif type(config) == dict:
            formatter = Formatter(config=_create_config_from_dict(config))
        else:
            raise Exception('Unsupported config type')
    _format_file(filename, formatter, inplace)

def format_query(query, config=Config()):
    if type(config) == type(Config()):
        formatter = Formatter(config=config)
    else:
        if type(config) == str:
            if config.startswith('{'):
                config = eval(config)
                formatter = Formatter(config=_create_config_from_dict(config))
            else:
                formatter = Formatter(config=_create_config_from_file(config))
        elif type(config) == dict:
            formatter = Formatter(config=_create_config_from_dict(config))
        else:
            raise Exception('Unsupported config type')
    return _format_query(query, formatter)

def _format_file(filename, formatter, inplace=False):
    query = _read_from_file(filename)
    reformattedQuery = _format_query(query, formatter)
    if inplace: # overwrite file
        logger.info('Writing to ' + filename + '...')
        _write_to_file(reformattedQuery, filename)
    else: # write to stdout
        sys.stdout.write(reformattedQuery)

def _read_from_file(filename):
    with codecs.open(filename=filename, mode='r', encoding='utf-8') as f:
        text = f.read()
    return text

def _write_to_file(reformattedQuery, filename):
    with codecs.open(filename=filename, mode='w', encoding='utf-8') as f:
        f.write(reformattedQuery)

def _format_query(query, formatter):
    return formatter.format(query)

def _create_config_from_dict(configDict, defaultConfigSection=DEFAULT_CONFIG_SECTION):
    '''
    Create Config object from dictionary, with extra handling for boolean values if the dictionary is converted from string.
    '''
    configParser = configparser.ConfigParser()
    configParser.optionxform = str # makes the parser case-sensitive
    if defaultConfigSection not in configDict:
        configDict = {defaultConfigSection: configDict}
    configParser.read_dict(configDict)
    args = {}
    args = _parse_args_in_correct_type(args, configParser, defaultConfigSection)
    config = Config(**args)
    return config

def _create_config_from_file(configFilename, defaultConfigSection=DEFAULT_CONFIG_SECTION):
    '''
    Read config from a config file and return a dictionary.
    '''
    configParser = configparser.ConfigParser()
    configParser.optionxform = str # makes the parser case-sensitive
    configParser.read(configFilename)
    if defaultConfigSection in configParser:
        configDict = {}
        configDict = _parse_args_in_correct_type(configDict, configParser, defaultConfigSection)
        return Config(**configDict)
    else:
        raise Exception('Section ' + defaultConfigSection + 'not found in ' + configFilename)
    
def _parse_args_in_correct_type(args, configParser, defaultConfigSection=DEFAULT_CONFIG_SECTION):
    '''
    Parse paramters in config with special handling for boolean values if config is converted from string.
    '''
    for key in configParser[defaultConfigSection]:
        args[key] = ast.literal_eval(configParser[defaultConfigSection][key])
    return args
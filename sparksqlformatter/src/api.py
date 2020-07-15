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
from __future__ import print_function  # for print() in Python 2
from io import open  # for open() in Python 2
import sys
import re
import logging
import configparser
import ast

from sparksqlformatter.src.config import Config
from sparksqlformatter.src.formatter import Formatter
from sparksqlformatter.src.sparksql_config import DEFAULT_CONFIG_SECTION

logger = logging.getLogger(__name__)
log_formatter = '[%(asctime)s] %(levelname)s [%(filename)s:%(lineno)s:%(funcName)s] %(message)s'
logging.basicConfig(stream=sys.stdout, level=logging.INFO, format=log_formatter)


def format_file(filePath, config=Config(), inPlace=False):
    '''
    Format given file with given configurations.

    Parameters
    filePath: string
        Path to the file to format.
    config: string, dict, or sparksqlformatter.src.config.Config() object
        Configurations for the query language.
    inPlace: bool
        If True, will format the file in place.
        Else, will write the formatted file to stdout.
    '''
    if type(config) == type(Config()):  # config is a Config() object
        formatter = Formatter(config=config)
    else:  # create Config() object from config
        if type(config) == str:
            if config.startswith('{'):  # config is a dictionary in string
                config = eval(config)
                formatter = Formatter(config=_create_config_from_dict(config))
            else:  # config is a file path
                formatter = Formatter(config=_create_config_from_file(config))
        elif type(config) == dict:  # config is a dictionary
            formatter = Formatter(config=_create_config_from_dict(config))
        else:
            raise Exception('Unsupported config type')
    _format_file(filePath, formatter, inPlace)


def format_query(query, config=Config()):
    '''
    Format query using given configurations.

    Parameters
    query: string
        The query to be formatted.
    config: string, dict, or sparksqlformatter.src.config.Config() object
        Configurations for the query language.
    
    Return: string
        The formatted query.
    '''
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


def _create_config_from_dict(configDict, defaultConfigSection=DEFAULT_CONFIG_SECTION):
    '''
    Create Config() object from dictionary.

    Parameters
    configDict: dict
        A dictionary of configurations specified in key-value pairs.
    defaultConfigSection: string
        The top-level config section that needs to be added on top of the configDict before feeding to configParser.read_dict(), default to 'sparksqlformatter'.
    
    Return: sparksqlformatter.src.config.Config() object
        The Config() object created from configDict.
    '''
    configParser = configparser.ConfigParser()
    configParser.optionxform = str  # makes the parser case-sensitive
    if defaultConfigSection not in configDict:
        configDict = {defaultConfigSection: configDict}  # add top-level section
    configParser.read_dict(configDict)  # configParser assumes the existence of a top-level section
    args = _parse_args_in_correct_type(configParser, defaultConfigSection)
    config = Config(**args)
    return config


def _create_config_from_file(configFilePath, defaultConfigSection=DEFAULT_CONFIG_SECTION):
    '''
    Create Config() object from config file.

    Parameters
    configFilePath: string
        Path to the config file.
    defaultConfigSection: string
        The top-level config section that needs to be added on top of the configDict before feeding to configParser.read_dict(), default to 'sparksqlformatter'.
    
    Return: sparksqlformatter.src.config.Config() object
        The Config() object created from the config file.
    '''
    configParser = configparser.ConfigParser()
    configParser.optionxform = str  # makes the parser case-sensitive
    configParser.read(configFilePath)
    if defaultConfigSection in configParser:
        configDict = _parse_args_in_correct_type(configParser, defaultConfigSection)
        return Config(**configDict)
    else:
        raise Exception('Section ' + defaultConfigSection + 'not found in ' + configFilePath)


def _parse_args_in_correct_type(configParser, defaultConfigSection=DEFAULT_CONFIG_SECTION):
    '''
    Parse paramters in config with special handling to convert boolean values converted from string back to boolean type.

    Parameters
    configParser: a configParser.ConfigParser() object
        Parser for config files.
    defaultConfigSection: string
        The top-level config section that needs to be added on top of the configDict before feeding to configParser.read_dict(), default to 'sparksqlformatter'.
    
    Return: dict
        A dictionary of configuration key-value pairs where values are of correct type.
    '''
    args = {}
    for key in configParser[defaultConfigSection]:
        args[key] = ast.literal_eval(configParser[defaultConfigSection][key])
    return args

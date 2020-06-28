from __future__ import print_function # for print() in Python 2
import sys
import re
import codecs
import logging
import configparser

from hiveqlformatter.src.core.config import Config
from hiveqlformatter.src.languages.hiveql_config import DEFAULT_CONFIG_SECTION

logger = logging.getLogger(__name__)
log_formatter = '[%(asctime)s] %(levelname)s [%(filename)s:%(lineno)s:%(funcName)s] %(message)s'
logging.basicConfig(stream=sys.stdout, level=logging.INFO, format=log_formatter)

def format_file(filename, formatter, inplace=False):
    query = read_from_file(filename)
    reformattedQuery = format_query(query, formatter)
    if inplace: # overwrite file
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

def format_query(query, formatter):
    return formatter.format(query)

def create_config_from_dict(configDict, defaultConfigSection=DEFAULT_CONFIG_SECTION):
    '''
    Create Config object from dictionary, with extra handling for boolean values if the dictionary is converted from string.
    '''
    configParser = configparser.ConfigParser()
    configParser.optionxform = str # makes the parser case-sensitive
    if defaultConfigSection not in configDict:
        configDict = {defaultConfigSection: configDict}
    configParser.read_dict(configDict)
    args = {}
    args = parse_args_with_bool(args, configParser, defaultConfigSection)
    config = Config(**args)
    return config

def create_config_from_file(configFilename, defaultConfigSection=DEFAULT_CONFIG_SECTION):
    '''
    Read config from a config file and return a dictionary.
    '''
    configParser = configparser.ConfigParser()
    configParser.optionxform = str # makes the parser case-sensitive
    configParser.read(configFilename)
    if defaultConfigSection in configParser:
        configDict = {}
        configDict = parse_args_with_bool(configDict, configParser, defaultConfigSection)
        return Config(**configDict)
    else:
        raise Exception('Section ' + defaultConfigSection + 'not found in ' + configFilename)
    
def parse_args_with_bool(args, configParser, defaultConfigSection=DEFAULT_CONFIG_SECTION):
    '''
    Parse paramters in config with special handling for boolean values if config is converted from string.
    '''
    for key in configParser[defaultConfigSection]:
        if key == 'reservedKeywordUppercase':
            args[key] = configParser.getboolean(defaultConfigSection, key) == 'True'
        else:
            args[key] = configParser[defaultConfigSection][key]
    return args
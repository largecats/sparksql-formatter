# hiveqlformatter
A [Hive Query Language](https://cwiki.apache.org/confluence/display/Hive/LanguageManual) formatter in Python based on [sql-formatter](https://github.com/zeroturnaround/sql-formatter) and its fork [sql-formatter-plus](https://github.com/kufii/sql-formatter-plus) (both are licensed under the MIT license), with customizations and extra features. The built-in formatter is for HiveQL queries, but can be easily extended to other query languages with similar structure by setting [language attributes](#language-attributes).

- [hiveqlformatter](#hiveqlformatter)
- [Installation](#installation)
  - [Install using pip](#install-using-pip)
  - [Install from source](#install-from-source)
- [Compatibility](#compatibility)
- [Usage](#usage)
  - [Use as command-line tool](#use-as-command-line-tool)
  - [Use as Python library](#use-as-python-library)
- [Language attributes](#language-attributes)

# Installation

## Install using pip
View package at https://test.pypi.org/project/hiveqlformatter-largecats/.
```
python3 -m pip install --index-url https://test.pypi.org/simple/ --no-deps hiveqlformatter-largecats
```
TBD:
```
pip install hiveqlformatter
```

## Install from source
See [here](https://docs.python.org/2/install/index.html#splitting-the-job-up).
```
python setup.py install
```

# Compatibility
Supports Python 2.7 and 3.6+.

# Usage
`hiveqlformatter` can be used as either a command-line tool or a Python library.

## Use as command-line tool
```
usage: hiveqlformatter [-h] [-files FILES [FILES ...]] [-i] [--config CONFIG]

Formatter for HiveQL queries.

optional arguments:
  -h, --help            show this help message and exit
  -files FILES [FILES ...]
                        Paths to files to format.
  -i, --in-place        Format the files in place.
  --config CONFIG       Configurations for the query language. Can be a path to a config file or a dictionary.
```

**Configurations**   
The `--config` argument specifies attributes of the query language, such as keywords, comment prefix, and indent. Supported language attributes can be found [at the end of this document](#language-attributes).

It accepts the following inputs:   
* Path to a config file:   
The config file should have section `[hiveqlformatter]` and key-value pairs specifying attributes, if needed. E.g.,
```
[hiveqlformatter]
reservedKeywordUppercase = False
linesBetweenQueries = 2
```
* Dictionary of configurations expressed as key-value pairs:   
E.g.,
```
$ hiveqlformatter --config="{'reservedKeywordUppercase': False}" -files <path_to_file1> <path_to_file2>
```

## Use as Python library
The module can also be used as a Python library.

Call `hiveqlformatter.api.format_query()` to format query in string:
```
>>> from hiveqlformatter import HiveQlFormatter, api
>>> formatter = HiveQlFormatter()
>>> query = 'select c1 from t1'
>>> api.format_query(query, formatter)
'SELECT\n    c1\nFROM\n    t0'
```
Call `hiveql.formatter.api.format_file()` to format query in file:
```
>>> from hiveqlformatter import HiveQlFormatter, api
>>> formatter = HiveQlFormatter()
>>> api.format_file(<path_to_file>, formatter, inplace=False)
...
```

**Configurations**   
Configurations can be specified as follows:
```
>>> formatter = HiveQlFormatter(config)
```
Similar to the command-line tool, there are two ways to create configurations when using `hiveqlformatter` as a Python library:   
* Path to a config file:   
Call `api.create_config_from_file` to parse configurations from a config file with section heading `hiveqlformatter`.
```
>>> from hiveqlformatter import HiveQlFormatter, Config, api
>>> config = api.create_config_from_file(<path_to_config_file>)
>>> formatter = HiveQlFormatter(config)
>>> query = 'select c1 FROM t0'
>>> api.format_query(query, formatter)
'select\n    c1\nfrom\n    t0'
```
* Dictionary:   
Call `api.create_config_from_dict` to parse configurations from a dictionary.
```
>>> from hiveqlformatter import HiveQlFormatter, Config, api
>>> config = api.create_config_from_dict({'reservedKeywordUppercase': False}, 'hiveqlformatter')
>>> formatter = HiveQlFormatter(config)
>>> query = 'select c1 FROM t0'
>>> formatter.format(query)
...
```

# Language attributes
**`keywords`**   

A list of keywords in the query language. E.g., `SELECT`, `FROM`, `from_unixtime()`. Default to HiveQL's [keywords](https://cwiki.apache.org/confluence/display/Hive/LanguageManual+DDL) and [functions](https://cwiki.apache.org/confluence/display/Hive/LanguageManual+UDF).

**`reservedKeywords`**   

A list of reserved keywords in the query language. Default to HiveQL's [reserved keywords](https://cwiki.apache.org/confluence/display/Hive/LanguageManual+DDL).

**`topLevelKeywords`**   

A list of keywords that should start a query block when formatting. E.g.,
```sql
SELECT
    [block]
FROM
    [block]
```
Default to
```python
TOP_LEVEL_KEYWORDS = [
        'ADD',
        'AFTER',
        'ALTER COLUMN',
        'ALTER TABLE',
        'DELETE FROM',
        'EXCEPT',
        'FETCH FIRST',
        'FROM',
        'GROUP BY',
        'GO',
        'HAVING',
        'INSERT INTO',
        'INSERT',
        'LIMIT',
        'MODIFY',
        'ORDER BY',
        'SELECT',
        'SET CURRENT SCHEMA',
        'SET SCHEMA',
        'SET',
        'UPDATE',
        'VALUES',
        'WHERE'
    ]
```

**`topLevelKeywordsNoIndent`**   

A list of top-level keywords that should not be indented when formatting. E.g., `UNION` in
```sql
SELECT
    ...
FROM
    ...
UNION
SELECT
    ...
FROM
    ...
```
Default to
```Python
TOP_LEVEL_KEYWORDS_NO_INDENT = [
        'INTERSECT',
        'INTERSECT ALL',
        'MINUS',
        'UNION',
        'UNION ALL'
    ]
```

**`newlineKeywords`**   

A list of keywords that should start a newline when formatting. E.g., `LEFT JOIN` in
```sql
SELECT
    ...
FROM
    t0
    LEFT JOIN t1 ...
    LEFT JOIN t2 ...
```
Note that this is less restrictive than `topLevelKeywords`, since top-level keywords always start a newline.
Default to
```python
NEWLINE_KEYWORDS = [
        'AND',
        'CROSS JOIN',
        'ELSE',
        'INNER JOIN',
        'JOIN',
        'LEFT JOIN',
        'LEFT OUTER JOIN',
        'OR',
        'OUTER JOIN',
        'RIGHT JOIN',
        'RIGHT OUTER JOIN',
        'THEN',
        'WHEN',
        'XOR'
    ]
```

**`stringTypes`**   

A list of character pairs that enclose strings in the query language. Default to
```python
['""', "N''", "''", '[]']
```

**`openParens`**   

A list of strings that behave as opening parentheses in the query language. Default to
```python
['(', 'CASE']
```

**`closeParens`**   

A list of strings that behave as closing parentheses in the query language. Default to
```python
[')', 'END']
```

**`lineCommentTypes`**   

A list of prefixes to comments in the query language. Default to
```python
['--']
```

**`reservedKeywordUppercase`**   

A boolean indicating whether the keywords should be converted to uppercase when formatting. Default to `True`.

**`linesBetweenQueries`**   

An integer that specifies the number of blank lines to put between (sub-)queries when formatting. E.g., with `linesBetweenQueries = 1`,
```sql
WITH t0 AS (
    ...
),

t1 AS (
    ...
)

SELECT
    ...
FROM
    ...
```

**`specialWordChars`**   

A list of characters that require special handling when formatting. Default to `[]`.

**`indent`**   

A string that specifies one indent. Default to four blanks:
```python
'    '
```


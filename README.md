# sparksqlformatter
A [SparkSQL](http://spark.apache.org/docs/latest/sql-ref.html) formatter in Python based on [sql-formatter](https://github.com/zeroturnaround/sql-formatter) and its fork [sql-formatter-plus](https://github.com/kufii/sql-formatter-plus), with customizations and extra features.

- [sparksqlformatter](#sparksqlformatter)
- [Installation](#installation)
  - [Install using pip](#install-using-pip)
  - [Install from source](#install-from-source)
- [Compatibility](#compatibility)
- [Usage](#usage)
  - [Use as command-line tool](#use-as-command-line-tool)
  - [Use as Python library](#use-as-python-library)
- [Style configurations](#style-configurations)

# Installation

## Install using pip
```
pip install sparksqlformatter
```

## Install from source
1. Download source code.
2. Navigate to the source code directory.
3. Do `python setup.py install` or `pip install .`.

# Compatibility
Supports Python 2.7 and 3.6+.

# Usage
`sparksqlformatter` can be used as either a command-line tool or a Python library.

## Use as command-line tool
```
usage: sparksqlformatter [-h] [-f FILES [FILES ...]] [-i] [--style STYLE]

Formatter for SparkSQL queries.

optional arguments:
  -h, --help            show this help message and exit
  -f FILES [FILES ...], --files FILES [FILES ...]
                        Paths to files to format.
  -i, --in-place        Format the files in place.
  --style STYLE         Style configurations for SparkSQL. Can be a path to a style config file or a dictionary.
```

**Style**   

The `--style` argument specifies foramtting style. Supported language attributes can be found in [style configurations](#style-configurations).

There are two ways to specify style:  
* Path to a style config file. E.g.,
```
$ sparksqlformatter --style="<path_to_config_file>" -f <path_to_file1> <path_to_file2>
```
The style config file should have section `[sparksqlformatter]` and key-value pairs specifying attributes. E.g.,
```
[sparksqlformatter]
reservedKeywordUppercase = False
linesBetweenQueries = 2
```
* Dictionary of configurations expressed as key-value pairs. E.g.,
```
$ sparksqlformatter --style="{'reservedKeywordUppercase': False}" -f <path_to_file1> <path_to_file2>
```

## Use as Python library

Call `sparksqlformatter.api.format_query()` to format query in string:
```
>>> from sparksqlformatter import api
>>> query = 'select c1 from t1'
>>> api.format_query(query)
'SELECT\n    c1\nFROM\n    t0'
```
Call `hiveql.formatter.api.format_file()` to format query in file:
```W
>>> from sparksqlformatter import api
>>> api.format_file(<path_to_file>, inPlace=False)
...
```

**Style**   

Formatting style can be specified via the `style` parameter in the api format functions.

Similar to the command-line tool, there are two ways to create configurations when using `sparksqlformatter` as a Python library:   
* Path to a style config file
```
>>> from sparksqlformatter import api
>>> style = '<path_to_config_file>'
>>> query = 'select c1 FROM t0'
>>> api.format_query(query, style)
...
```
* Dictionary
```
>>> from sparksqlformatter import api
>>> style = {'reservedKeywordUppercase': False}
>>> query = 'select c1 FROM t0'
>>> api.format_query(query, style)
'select\n    c1\nfrom\n    t0'
```

# Style configurations

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
    'ADD', 'AFTER', 'ALTER COLUMN', 'ALTER TABLE', 'CREATE TABLE', 'CROSS JOIN', 'DELETE FROM', 'EXCEPT',
    'FETCH FIRST', 'FROM', 'GROUP BY', 'GO', 'HAVING', 'INNER JOIN', 'INSERT INTO', 'INSERT', 'JOIN',
    'LEFT JOIN', 'LEFT OUTER JOIN', 'LIMIT', 'MODIFY', 'ORDER BY', 'OUTER JOIN', 'PARTITION BY', 'RIGHT JOIN',
    'RIGHT OUTER JOIN', 'SELECT', 'SET CURRENT SCHEMA', 'SET SCHEMA', 'SET', 'UPDATE', 'VALUES', 'WHERE'
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
TOP_LEVEL_KEYWORDS_NO_INDENT = ['INTERSECT', 'INTERSECT ALL', 'MINUS', 'UNION', 'UNION ALL']
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
    'AND', 'ELSE', 'LATERAL', 'ON', 'OPTIONS', 'OR', 'PARTITIONED BY', 'THEN', 'USING', 'WHEN', 'XOR'
]
```

**`stringTypes`**   

A list of character pairs that enclose strings in the query language. Default to
```python
['""', "''", '{}', '``']
```

**`openParens`**   

A list of strings that behave as opening parentheses in the query language regarding block indent level. Default to
```python
['(', '[', 'CASE']
```

**`closeParens`**   

A list of strings that behave as closing parentheses in the query language regarding block indent level. Default to
```python
[')', ']', 'END']
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

**`inlineMaxLength`**    

Maximum length of an inline block. Default to `120`.

**`splitOnComma`**    

If true, in cases where a comma separated list in `GROUP BY`, `ORDER BY` clauses is too long to fit in a line, split such that all elements are on a single line.
Else, will only split at `inlineMaxLength`.
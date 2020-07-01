# Change Log

## 2020-06-24
Added source code, translated from JavaScript in [sql-formatter](https://github.com/zeroturnaround/sql-formatter) and its fork [sql-formatter-plus](https://github.com/kufii/sql-formatter-plus) to Python.

## 2020-06-25
1. Added customized tests.
2. Added constraints to not add `\n` before reserved keywords `AND`, `OR` if the previous keyword is `BETWEEN`, `WHEN`, or `ON`.
3. Added blank line between sub-queries. The number of blank lines is customizable via `-linesBetweenQueries`.
4. Added command-line interface.

## 2020-06-27
1. Added api module to interact with scripts and configuration files.
2. Updated `__init__` file to use the api module to parse configurations.

## 2020-07-02
1. Added wrapper functions to api module so that users don't need to create formatter, instead, just pass the config as arguement to `format_file()`, `format_query()`.
2. Updated `__init__` and tests accordingly.
3. Put files in `core` and `languages` directly under `src`. Removed file `hiveql_formatter.py`.
4. Added feature to remove space after `-` when it is used as negative sign isntead of minus sign.
5. Added feature to remove space after `{` and space before `}` for string formatting.
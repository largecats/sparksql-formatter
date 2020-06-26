# hiveql-formatter
A HiveQL formatter in Python based on [sql-formatter](https://github.com/zeroturnaround/sql-formatter) and its fork [sql-formatter-plus](https://github.com/kufii/sql-formatter-plus), with customizations and extra features. Both [sql-formatter](https://github.com/zeroturnaround/sql-formatter) and [sql-formatter-plus](https://github.com/kufii/sql-formatter-plus) are licensed under the MIT license.

## Install

## Usage

### Command-line
```
$ hiveql-formatter
```
```
hiveql-formatter --config="{'reservedKeywordUppercase': False}" -files <path_to_file>
```

### Python library
```python
import hqlf
```
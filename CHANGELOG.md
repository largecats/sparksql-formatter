# Change Log

## 2020-06-24
Added source code, translated from JavaScript in [sql-formatter](https://github.com/zeroturnaround/sql-formatter) and its fork [sql-formatter-plus](https://github.com/kufii/sql-formatter-plus) to Python.

## 2020-06-25
Added customized tests.

## 2020-06-25
1. Added constraints to not add `\n` before reserved keywords `AND`, `OR` if the previous keyword is `BETWEEN`, `WHEN`, or `ON`.
2. Added blank line between sub-queries. The number of blank lines is customizable via `-linesBetweenQueries`.
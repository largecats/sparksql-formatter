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

## 2020-07-07
1. Added extra handling to treat text enclosed by `{}` (Python string formatting keyword) as string in the query language, so that query language keywords enclosed by `{}` are ignored. E.g., for newline keyword `CREATE`, the text `{CREATE}` is not formatted as 
```
{
    CREATE
}
```
Added test.
2. Fixed bug in minus sign formatting. Added test.

## 2020-07-08
1. Removed `\n` before line comment after comma so that the comment can be kept on the same line as the query.
2. Made `inlineMaxLength` a customizable parameter in `Config()`.
3. Added `JOIN` keywords to `TOP_LEVEL_KEYWORDS` and `ON` to `NEWLINE_KEYWORDS`.

## 2020-07-14
1. Added support for user-defined functions.
2. Fixed bug in `subQuery`, where the closing parenthesis in `foo(c1)` in `select foo(c1), c2 from t0` is treated as the closing parenthesis of a `subQuery`.

## 2020-07-19
1. Separated config and style to hide keywords and functions in config from users. Only style is customizable.

## 2020-08-13
1. Added `[]` to `openParens`, `closeParens` in `style.py`. Added tests.

## 2020-08-14
1. Added `splitOnComma` parameter that decides whether to split on each comma in GROUP BY, ORDER BY clauses. Added tests for GROUP BY and ORDER BY.

## 2020-08-15
1. Changed from checking second last token to checking the last keyword when identifying the start of subquery. This is to make sure the subquery's opening parenthsis can be identified when there is comment between keyword `AS` and the opening parenthesis.

## 2020-08-18
1. Added `previousTopLevelKeyword` attribute to formatter to keep track of top-level keywords to use in formatting comma under `GROUP BY`, `ORDER BY` clauses.
2. Import `configparser` from `backports` if on Python 2. See https://github.com/takluyver/entrypoints/issues/3.

## 2020-08-27
1. In subquery formatting, limit opening/closing parenthese to `(`, `)`; `CASE`, `END`, and `[`, `]` are not treated as opening/closing parentheses.

## 2020-08-28
1. Put `UNION ALL` and `INTERSECT ALL` in front of `UNION`, `INTERSECT` in `config.TOP_LEVEL_KEYWORDS_NO_INDENT` to make sure that `UNION ALL`, `INTERSECT ALL` are recognized as single keywords and thus formatted on the same line.

## 2020-09-01
1. Moved `MSCK`, `PARTITIONED` from non-reserved keywords to reserved keywords.
2. Added `WHEN`, `THEN`, `ELSE` to `topLevelKeywords`.
3. Updated `format_newline_keyword()` logic to put `AND`, `OR` in `CASE...WHEN` on newline.
4. Added back ticks to `stringTypes`.

## 2020-10-11
1. Updated logic for finding the start of sub-queries.
2. Added test `test_operator_with_parentheses`.
3. Updated test `test_query_with_subquery_inline_comment` to put command after opening parenthesis of the sub-query.

## 2021-06-24
1. Added test for query with string regex containing operators. Spaces should not be added before and after the operators inside string regex enclosed with backticks.

## 2021-06-25
1. Updated `_parse_args_in_correct_type()` logic to exclude parsing the value of `indent` key when defining style using a dictionary. See https://github.com/largecats/sparksql-formatter/issues/72.
2. Added test for setting indent style via dictionary.
3. Updated tests to use unittest library.
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
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
import logging
from hqlf.src.languages.hiveql_formatter import HiveQlFormatter

logger = logging.getLogger(__name__)
log_formatter = '[%(asctime)s] %(levelname)s [%(filename)s:%(lineno)s:%(funcName)s] %(message)s'
logging.basicConfig(stream=sys.stdout, level=logging.INFO, format=log_formatter)
logger.info('Script loaded...')

class Test:

    def __init__(self):
        self.formatter = HiveQlFormatter()
    
    def run(self, msg, testQuery, key):
        logger.info(msg)
        formattedQuery = self.formatter.format(testQuery)
        logger.info('formattedQuery =')
        logger.info(formattedQuery)
        logger.info(repr(formattedQuery))
        logger.info('key =')
        logger.info(key)
        logger.info(repr(key))
        assert formattedQuery == key
        return True
    
    def test_short_create_table(self):
        msg = 'Testing short CREATE TABLE'
        testQuery = 'CREATE TABLE t0 (a INT PRIMARY KEY, b STRING)'
        key = 'CREATE TABLE t0 (a INT PRIMARY KEY, b STRING)'
        return self.run(msg, testQuery, key)
    
    def test_long_create_table(self):
        msg = 'Testing long CREATE TABLE'
        testQuery = '''
CREATE TABLE t0 (a INT PRIMARY KEY, b STRING, c INT NOT NULL, d INT NOT NULL,
e INT NOT NULL, f INT NOT NULL, g INT NOT NULL, h INT NOT NULL, i INT NOT NULL, j INT NOT NULL)
'''
        key = '''
CREATE TABLE t0 (
    a INT PRIMARY KEY,
    b STRING,
    c INT NOT NULL,
    d INT NOT NULL,
    e INT NOT NULL,
    f INT NOT NULL,
    g INT NOT NULL,
    h INT NOT NULL,
    i INT NOT NULL,
    j INT NOT NULL
)
        '''.strip()
        return self.run(msg, testQuery, key)

    def test_insert_without_into(self):
        msg = 'Testing INSERT without INTO'
        testQuery = '''INSERT Customers (ID, MoneyBalance, Address, City) VALUES (12, -123.4, 'Skagen 2111','Stv')'''
        key = '''
INSERT
    Customers (ID, MoneyBalance, Address, City)
VALUES
    (12, -123.4, 'Skagen 2111', 'Stv')
        '''.strip()
        return self.run(msg, testQuery, key)
    
    def test_alter_table_modify(self):
        msg = 'Testing ALTER TABLE ... MODIFY query'
        testQuery = '''ALTER TABLE supplier MODIFY supplier_name STRING(100) NOT NULL'''
        key = '''
ALTER TABLE
    supplier
MODIFY
    supplier_name STRING(100) NOT NULL
        '''.strip()
        return self.run(msg, testQuery, key)

    def test_alter_table_alter_column(self):
        msg = 'Testing ALTER TABLE ... ALTER COLUMN query'
        testQuery = '''ALTER TABLE supplier ALTER COLUMN supplier_name STRING(100) NOT NULL'''
        key = '''
ALTER TABLE
    supplier
ALTER COLUMN
    supplier_name STRING(100) NOT NULL
        '''.strip()
        return self.run(msg, testQuery, key)
    
    def test_select_with_cross_join(self):
        msg = 'Testing SELECT query with LEFT JOIN'
        testQuery = '''SELECT a, b FROM t LEFT JOIN t2 ON t.id = t2.id_t'''
        key = '''
SELECT
    a,
    b
FROM
    t
    LEFT JOIN t2 ON t.id = t2.id_t
        '''.strip()
        return self.run(msg, testQuery, key)

    def test_simple_select(self):
        msg = 'Testing simple SELECT'
        testQuery = '''SELECT c1, c2 FROM t0'''
        key = '''
SELECT
    c1,
    c2
FROM
    t0
        '''.strip()
        return self.run(msg, testQuery, key)
    
    def test_case_when(self):
        msg = 'Testing CASE ... WHEN'
        testQuery = '''SELECT c1, c2, CASE WHEN c3 = 'one' THEN 1 WHEN c3 = 'two' THEN 2 ELSE 3 END AS c4 FROM t0'''
        key = '''
SELECT
    c1,
    c2,
    CASE
        WHEN c3 = 'one'
        THEN 1
        WHEN c3 = 'two'
        THEN 2
        ELSE 3
    END AS c4
FROM
    t0
        '''.strip()
        return self.run(msg, testQuery, key)
    
    def test_case_when_with_expression(self):
        msg = 'Testing CASE ... WHEN with expression'
        testQuery = '''
SELECT
CASE WHEN toString(getNumber()) = 'one' THEN 1
WHEN toString(getNumber()) = 'two' THEN 2 ELSE 3 END AS c1
FROM t0
'''
        key = '''
SELECT
    CASE
        WHEN toString(getNumber()) = 'one'
        THEN 1
        WHEN toString(getNumber()) = 'two'
        THEN 2
        ELSE 3
    END AS c1
FROM
    t0
        '''.strip()
        return self.run(msg, testQuery, key)

    def test_lowercase_case_when(self):
        msg = 'Testing lower-case CASE ... WHEN'
        testQuery = '''select case when c1 = 'foo' then 1 else 2 end from t0'''
        key = '''
SELECT
    CASE
        WHEN c1 = 'foo'
        THEN 1
        ELSE 2
    END
FROM
    t0
        '''.strip()
        return self.run(msg, testQuery, key)
    
    def test_ignore_case_when_in_other_string(self):
        msg = 'Testing ignore CASE, WHEN in other strings'
        testQuery = '''SELECT CASEDATE, ENDDATE FROM table1'''
        key = '''
SELECT
    CASEDATE,
    ENDDATE
FROM
    table1
        '''.strip()
        return self.run(msg, testQuery, key)
    
    def test_line_comment(self):
        msg = 'Testing line comment'
        testQuery = '''
SELECT a,--comment, here
b FROM t0--comment'''
        key = '''
SELECT
    a,
    --comment, here
    b
FROM
    t0 --comment
        '''.strip()
        return self.run(msg, testQuery, key)
    
    def test_line_comment_followed_by_comma(self):
        msg = 'Testing line comment followed by comma'
        testQuery = '''
SELECT a --comment
, b
        '''
        key = '''
SELECT
    a --comment
,
    b
        '''.strip()
        return self.run(msg, testQuery, key)
    
    def test_line_comment_followed_by_close_paren(self):
        msg = 'Testing line comment followed by closing parentheses'
        testQuery = '''
SELECT ( a --comment
 )
        '''
        key = '''
SELECT
    (
        a --comment
    )
        '''.strip()
        return self.run(msg, testQuery, key)
    
    def test_line_comment_followed_by_open_paren(self):
        msg = 'Testing line comment followed by opening parentheses'
        testQuery = '''
SELECT a --comment
()
        '''
        key = '''
SELECT
    a --comment
    ()
        '''.strip()
        return self.run(msg, testQuery, key)
    
    def test_query_with_between_and(self):
        msg = 'Testing query with BETWEEN ... AND'
        testQuery = '''
select c1, c2 from t0
where c1 between '{date}' and add_months('{date}', 1)
and c2 < 0
        '''
        key = '''
SELECT
    c1,
    c2
FROM
    t0
WHERE
    c1 BETWEEN '{date}' AND add_months('{date}', 1)
    AND c2 < 0
        '''.strip()
        return self.run(msg, testQuery, key)
    
    def test_query_with_left_join_and(self):
        msg = 'Testing query with LEFT JOIN ... AND'
        testQuery = '''
select c1, c2 from t0
left join t1 on t0.c1 = t1.c1 and t0.c3 = t1.c3
        '''
        key = '''
SELECT
    c1,
    c2
FROM
    t0
    LEFT JOIN t1 ON t0.c1 = t1.c1 AND t0.c3 = t1.c3
        '''.strip()
        return self.run(msg, testQuery, key)
    
    def test_query_with_nested_and_in_where(self):
        msg = 'Testing query with nested AND in WHERE'
        testQuery = '''
SELECT c1, c2 FROM t0 WHERE type = 1 OR (c3 = 0 AND type = 2)
        '''
        key = '''
SELECT
    c1,
    c2
FROM
    t0
WHERE
    type = 1
    OR (
        c3 = 0
        AND type = 2
    )
        '''.strip()
        return self.run(msg, testQuery, key)
    
    def test_query_with_long_table_name(self):
        msg = 'Testing query with long table name'
        testQuery = '''
select t0.a, t0.b, t1.x, t2.y,
    t3.c, t3.d

from t0_very_very_very_very_very_very_very_very_very_long_table_name t0
    left join t1_very_very_very_very_very_very_very_very_very_long_table_name t1 on t0.a = t1.z
    left join t2 on t0.a = t2.z

    left join t3 on t3.c = t0.a

where t0.a between '{date}' and add_months('{date}', 1)
and t2.y < 0
order by 1,2,3
        '''
        key = '''
SELECT
    t0.a,
    t0.b,
    t1.x,
    t2.y,
    t3.c,
    t3.d
FROM
    t0_very_very_very_very_very_very_very_very_very_long_table_name t0
    LEFT JOIN t1_very_very_very_very_very_very_very_very_very_long_table_name t1 ON t0.a = t1.z
    LEFT JOIN t2 ON t0.a = t2.z
    LEFT JOIN t3 ON t3.c = t0.a
WHERE
    t0.a BETWEEN '{date}' AND add_months('{date}', 1)
    AND t2.y < 0
ORDER BY
    1,
    2,
    3
        '''.strip()
        return self.run(msg, testQuery, key)
    
    def test_query_with_unicode_char(self):
        msg = 'Testing query with unicode character'
        testQuery = '''
select c1, c2 from t0
where t1.c2 IN ('你好' 'ไหว้')
        '''
        key = '''
SELECT
    c1,
    c2
FROM
    t0
WHERE
    t1.c2 IN ('你好' 'ไหว้')
        '''.strip()
        return self.run(msg, testQuery, key)
    
    def test_query_with_subquery(self):
        msg = 'Testing query with subquery'
        testQuery = '''
with t0 as (select c1, c2 from tab1),

t1 as (select c1, c2 from tab2),

t2 as (select c1, c2 from tab3)

select * from t0 left join t1 on t0.c1 = t1.c1
left join t2 on t0.c1 = t2.c1
        '''
        key = '''
WITH t0 AS (
    SELECT
        c1,
        c2
    FROM
        tab1
),

t1 AS (
    SELECT
        c1,
        c2
    FROM
        tab2
),

t2 AS (
    SELECT
        c1,
        c2
    FROM
        tab3
)

SELECT
    *
FROM
    t0
    LEFT JOIN t1 ON t0.c1 = t1.c1
    LEFT JOIN t2 ON t0.c1 = t2.c1
        '''.strip()
        return self.run(msg, testQuery, key)
    
    def run_all(self):
        tests = list(filter(lambda m: m.startswith('test_'), dir(self)))
        for test in tests:
            getattr(self, test)()

if __name__ == "__main__":
    Test().run_all()
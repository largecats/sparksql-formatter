import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from src.hiveql_formatter import HiveQlFormatter

class Test:

    def __init__(self):
        self.formatter = HiveQlFormatter()
    
    def run(self, msg, testQuery, key):
        print(msg + '\n')
        formattedQuery = self.formatter.format(testQuery)
        print('formattedQuery = \n')
        print(formattedQuery)
        print(repr(formattedQuery))
        print('key = \n')
        print(key)
        print(repr(key))
        assert formattedQuery == key
        return True
    
    def test_short_create_table(self):
        msg = 'Testing short CREATE TABLE'
        testQuery = 'CREATE TABLE t0 (a INT PRIMARY KEY, b STRING)'
        key = 'CREATE TABLE t0 (a INT PRIMARY KEY, b STRING)'
        return self.run(msg, testQuery, key)
    
    def test_long_create_table(self):
        msg = 'Testing long CREATE TABLE'
        testQuery = '''CREATE TABLE t0 (a INT PRIMARY KEY, b STRING, c INT NOT NULL, d INT NOT NULL)'''
        key = '''
CREATE TABLE t0 (
    a INT PRIMARY KEY,
    b STRING,
    c INT NOT NULL,
    d INT NOT NULL
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
        testQuery = '''CASE WHEN a = 'foo' THEN 1 WHEN a = 'bar' THEN 2 WHEN a = 'baz' THEN 3 ELSE 4 END'''
        key = '''
CASE
    WHEN a = 'foo' THEN 1
    WHEN a = 'bar' THEN 2
    WHEN a = 'baz' THEN 3
    ELSE 4
END
        '''.strip()
        return self.run(msg, testQuery, key)
    
    def test_case_when_inside_select(self):
        msg = 'Testing CASE ... WHEN inside SELECT'
        testQuery = '''SELECT c1, c2, CASE WHEN c3 = 'one' THEN 1 WHEN c3 = 'two' THEN 2 ELSE 3 END AS c4 FROM t0'''
        key = '''
SELECT
    c1,
    c2,
    CASE
        WHEN c3 = 'one' THEN 1
        WHEN c3 = 'two' THEN 2
        ELSE 3
    END AS c4
FROM
    t0
        '''.strip()
        return self.run(msg, testQuery, key)
    
    def test_case_when_with_expression(self):
        msg = 'Testing CASE ... WHEN with expression'
        testQuery = '''CASE WHEN toString(getNumber()) = 'one' THEN 1 WHEN toString(getNumber()) = 'two' THEN 2 ELSE 3 END'''
        key = '''
CASE
    WHEN toString(getNumber()) = 'one' THEN 1
    WHEN toString(getNumber()) = 'two' THEN 2
    ELSE 3
END
        '''.strip()
        return self.run(msg, testQuery, key)

    def test_lowercase_case_when(self):
        msg = 'Testing lower-case CASE ... WHEN'
        testQuery = '''case when c1 = 'foo' then 1 else 2 end'''
        key = '''
CASE
    WHEN c1 = 'foo' THEN 1
    ELSE 2
END
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
    
    def test_complex_query(self):
        msg = 'Testing complex query'
        testQuery = '''
select t0.a, t0.b, t1.x, t2.y,
    t3.c, t3.d

from t0
    left join t1 on t0.a = t1.z
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
    t0
    LEFT JOIN t1 ON t0.a = t1.z
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

    
    def test_complex_query_with_long_table_name(self):
        msg = 'Testing complex query'
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
    
    def run_all(self):
        tests = list(filter(lambda m: m.startswith('test_'), dir(self)))
        for test in tests:
            getattr(self, test)()

if __name__ == "__main__":
    Test().run_all()
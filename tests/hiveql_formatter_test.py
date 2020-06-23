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
        print(repr(formattedQuery))
        print('key = \n')
        print(repr(key))
        assert formattedQuery == key
        return True

msg = 'Testing short CREATE TABLE'
testQuery = 'CREATE TABLE items (a INT PRIMARY KEY, b STRING)'
key = 'CREATE TABLE items (a INT PRIMARY KEY, b STRING)'
Test().run(msg, testQuery, key)

msg = 'Testing long CREATE TABLE'
testQuery = '''CREATE TABLE items (a INT PRIMARY KEY, b STRING, c INT NOT NULL, d INT NOT NULL)'''
key = '''
CREATE TABLE items (
    a INT PRIMARY KEY,
    b STRING,
    c INT NOT NULL,
    d INT NOT NULL
)
'''.lstrip().rstrip()
Test().run(msg, testQuery, key)

msg = 'Testing INSERT without INTO'
testQuery = '''INSERT Customers (ID, MoneyBalance, Address, City) VALUES (12, -123.4, 'Skagen 2111','Stv')'''
key = '''
INSERT
    Customers (ID, MoneyBalance, Address, City)
VALUES
    (12, -123.4, 'Skagen 2111', 'Stv')
'''.lstrip().rstrip()
Test().run(msg, testQuery, key)


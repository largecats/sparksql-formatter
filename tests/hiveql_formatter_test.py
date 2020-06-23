import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from src.hiveql_formatter import HiveQlFormatter

class Test:

    def __init__(self):
        self.formatter = HiveQlFormatter()
        self.testQueries = [
            'CREATE TABLE items (a INT PRIMARY KEY, b STRING)'
        ]
        self.keys = [
            '''
            CREATE TABLE items (
                a INT PRIMARY KEY,
                b STRING
            )
            '''.lstrip().rstrip()
        ]
    
    def run(self):
        for i in range(len(self.testQueries)):
            query = self.testQueries[i]
            formattedQuery = self.formatter.format(query)
            key = self.keys[i]
            print 'formattedQuery = \n'
            print repr(formattedQuery)
            print 'key = \n'
            print repr(key)
            assert formattedQuery == key
        return True

Test().run()

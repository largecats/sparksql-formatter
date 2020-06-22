import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from src.hiveql_formatter import HiveQlFormatter

class Test:

    def __init__(self):
        self.formatter = HiveQlFormatter()
        self.testQueries = [
            'CREATE TABLE items (a INT PRIMARY KEY, b TEXT, c INT NOT NULL, d INT NOT NULL)'
        ]
        self.keys = [
            '''
            CREATE TABLE items (
                a INT PRIMARY KEY,
                b TEXT,
                c INT NOT NULL,
                d INT NOT NULL
            )
            '''
        ]
    
    def run(self):
        for i in range(len(self.testQueries)):
            query = self.testQueries[i]
            formattedQuery = self.formatter.format(query)
            print formattedQuery
            print keys[i]
            assert formattedQuery == keys[i]
        return True

Test().run()

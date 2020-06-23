import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from src.hiveql_formatter import HiveQlFormatter

class Test:

    def __init__(self):
        self.formatter = HiveQlFormatter()
        self.testQueries = [
            'SELECT a.c1 FROM a WHERE a.c2 IS NULL'
        ]
        self.keys = [
'''
SELECT
    a.c1
FROM
    a
WHERE
    a.c2 IS NULL
'''.lstrip().rstrip()
        ]
    
    def run(self):
        for i in range(len(self.testQueries)):
            query = self.testQueries[i]
            formattedQuery = self.formatter.format(query)
            print repr(formattedQuery)
            print repr(self.keys[i])
            assert formattedQuery == self.keys[i]
        return True

Test().run()

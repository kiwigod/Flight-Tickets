from parsers.objparser import ObjParser
import sqlite3


class DB:
    def __init__(self, table: str, cols: [str], database='flights.db'):
        self.conn = sqlite3.connect(database)
        self.c = self.conn.cursor()
        self.table = table
        self.cols = cols

    def get(self, _id: int):
        self.c.execute('SELECT * FROM %s WHERE id = ?' % self.table, [str(_id)])
        return self.c.fetchone()

    def insert(self):
        values = [ObjParser.parse(self.__dict__[x]) for x in self.cols]
        insert_cols = ','.join(self.cols)
        qs = ','.join(['?'] * len(self.cols))
        print('INSERT INTO %s (%s) VALUES (%s)' % (self.table, insert_cols, values))
        self.c.execute('INSERT INTO %s (%s) VALUES (%s)' % (self.table, insert_cols, qs), values)
        self.conn.commit()

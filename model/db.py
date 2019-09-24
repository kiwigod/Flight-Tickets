import sqlite3


class DB:
    def __init__(self, table: str, cols: [str], database='flights.db'):
        conn = sqlite3.connect(database)
        self.c = conn.cursor()
        self.table = table
        self.cols = cols

    def get(self, _id: int):
        self.c.execute('SELECT * FROM ? WHERE id = ?', [self.table, str(_id)])
        return self.c.fetchone()

    def insert(self):
        self.c.execute('INSERT INTO ? (?) VALUES (?)', [self.table, ','.join(self.cols),
                                                        ','.join([self.__dict__[x] for x in self.cols])])

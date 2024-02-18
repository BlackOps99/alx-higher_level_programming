#!/usr/bin/python3
"""  script that lists all cities from the database """
import MySQLdb
from sys import argv

if __name__ == '__main__':

    db = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                         passwd=argv[2], db=argv[3])

    cur = db.cursor()
    cur.execute("""SELECT c.id, c.name, s.name FROM
                cities c INNER JOIN states s ON s.id=c.state_id""")

    for i in cur.fetchall():
        print(i)

    cur.close()
    db.close()

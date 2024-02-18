#!/usr/bin/python3
""" Script get all states with a name starting with N (upper N) """
import MySQLdb
from sys import argv

if __name__ == '__main__':

    db = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                         passwd=argv[2], db=argv[3])

    cur = db.cursor()
    cur.execute("SELECT * FROM states WHERE name\
                LIKE BINARY 'N%' ORDER BY states.id")

    for i in cur.fetchall():
        print(i)

    cur.close()
    db.close()

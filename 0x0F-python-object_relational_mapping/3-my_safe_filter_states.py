#!/usr/bin/python3
"""  script that safe from the SQL Injection """
import MySQLdb
from sys import argv

if __name__ == '__main__':

    db = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                         passwd=argv[2], db=argv[3])

    cur = db.cursor()
    cur.execute("SELECT * FROM states WHERE BINARY name = %s", [argv[4]])

    for i in cur.fetchall():
        print(i)

    cur.close()
    db.close()

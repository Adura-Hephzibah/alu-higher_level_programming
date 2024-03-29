#!/usr/bin/python3
"""
Module 3-my_safe_filter_states.py
return matching states; safe from MySQL injections
# http://bobby-tables.com/python to learn about mysql injections
"""


import MySQLdb
from sys import argv


if __name__ == "__main__":
    conn = MySQLdb.connect(host="localhost", port=3306, charset="utf8",
                           user=argv[1], passwd=argv[2], db=argv[3])
    cur = conn.cursor()
    cur.execute("""SELECT * FROM states WHERE name= %s
                ORDER BY states.id ASC""", (argv[4], ))
    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)
    cur.close()
    conn.close()

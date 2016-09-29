import MySQLdb as mdb
import sys

DB_HOST = "localhost"
DB_USER = "frav"
DB_PASS = "VXxL4UOLvB6wc01Y3Cxi"
DB_NAME = "frav_ABC"

try:
    con = mdb.connect(DB_HOST, DB_USER, DB_PASS, DB_NAME);

    cur = con.cursor()
    cur.execute("SELECT VERSION()")

    ver = cur.fetchone()

    print("Database version : %s " % ver)

except mdb.Error as e:

    print("Error %d: %s" % (e.args[0], e.args[1]))
    sys.exit(1)

finally:

    if con:
        con.close()
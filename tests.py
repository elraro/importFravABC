import MySQLdb as mdb
import sys

DB_HOST = "localhost"
DB_USER = "frav"
DB_PASS = "VXxL4UOLvB6wc01Y3Cxi"
DB_NAME = "frav_ABC"

# con = None
#
# con = mdb.connect(DB_HOST, DB_USER, DB_PASS, DB_NAME)
# cur = con.cursor()
#
# try:
#     cur.execute(
#         "INSERT INTO " + DB_NAME + " VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,\
#          %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,\
#          %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,\
#          %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",
#         (188, 90))
#     con.commit()
# except:
#     print("error")
#     con.rollback()
#
# con.close()

a = "D:\SIBAR\FRAV_ABC\Logitech\fluorescente\Logitech_flu_009\Frames\Camera MEDIUM\frame_Logitech_flu_009_MED_014.jpg".replace("\f", "\\f")
a = a.split("\\")
print(a)


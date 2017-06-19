import MySQLdb as Mdb

# Hardcoded
DB_HOST = ""
DB_USER = ""
DB_PASS = ""
DB_NAME = ""
FOLDER = ""

con = Mdb.connect(DB_HOST, DB_USER, DB_PASS, DB_NAME)
cur = con.cursor()

cur.execute("SELECT * FROM score_data s INNER JOIN pass_data p ON s.id_pass = p.id INNER JOIN imgs_data i ON s.id_img = i.id WHERE s.id=3")
data = cur.fetchall()
for row in data:
    print(row)

cur.execute("SELECT f.id, f.clase, f.file, c.camera, l.light, f.frame FROM pass_data f INNER JOIN light_info l ON l.id = f.light INNER JOIN camera_info c ON c.id = f.camera WHERE f.id=1")
data = cur.fetchall()
for row in data:
    print(row)

cur.execute("SELECT i.id, i.clase, i.file, c.camera, l.light, i.frame FROM imgs_data i INNER JOIN light_info l ON l.id = i.light INNER JOIN camera_info c ON c.id = i.camera WHERE i.id=25932")
data = cur.fetchall()
for row in data:
    print(row)

cur.execute("SELECT * FROM score_data s INNER JOIN fir_data f ON s.id_fir = f.id INNER JOIN imgs_data i ON s.id_img = i.id WHERE i.light=4")
data = cur.fetchall()
for row in data:
    print(row)

con.close()
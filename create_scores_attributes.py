import MySQLdb as Mdb
import numpy as np
import dill

# Hardcoded
DB_HOST = ""
DB_USER = ""
DB_PASS = ""
DB_NAME = ""
FOLDER = ""

con = Mdb.connect(DB_HOST, DB_USER, DB_PASS, DB_NAME)
cur = con.cursor()

users = np.ndarray(shape=112, dtype=int)
attributes = np.ndarray(shape=(112, 112, 75), dtype=float)
scores = np.ndarray(shape=(112, 112), dtype=float)
attr_aux = np.ndarray(shape=(112, 75), dtype=float)  # aux
scores_aux = np.ndarray(shape=112, dtype=float)  # aux
# np.set_printoptions(threshold=np.nan)  # para debug

cur.execute("SELECT i.clase FROM `imgs_data` i WHERE i.camera = 1 AND i.light = 1 GROUP BY i.clase")
total_users = cur.fetchall()
for user in total_users:
    users[user[0]] = user[0]

# vamos a leer los atributos y a guardarlos en matrix
count_pass = 0
for user_pass in users:
    count_img = 0
    for user_img in users:
        cur.execute("SELECT * FROM `score_data` s INNER JOIN `imgs_data` i ON s.id_img = i.id WHERE s.id_pass = " + str(user_pass+1) + " AND i.clase = " + str(user_img) + " AND i.camera = 1 AND i.light = 1 ORDER BY s.score DESC LIMIT 1")
        row_data = cur.fetchall()
        attr_aux[count_img] = list(row_data[0][10:])
        scores_aux[count_img] = row_data[0][3]
        count_img += 1
    attributes[count_pass] = np.matrix(attr_aux)
    scores[count_pass] = np.matrix(scores_aux)
    count_pass += 1

# dump
dill.dump(scores, open("scores.bin", "wb"))
dill.dump(attributes, open("attributes.bin", "wb"))


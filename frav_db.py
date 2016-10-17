import MySQLdb as Mdb
import querys as querys
import sys

# Hardcoded
DB_HOST = "localhost"
DB_USER = "frav"
DB_PASS = "VXxL4UOLvB6wc01Y3Cxi"
DB_NAME = "frav_ABC"
FOLDER = "/media/alberto/Datos/FRAV_ALBERTO/"

con = Mdb.connect(DB_HOST, DB_USER, DB_PASS, DB_NAME)
cur = con.cursor()

cur.execute(querys.create_camera_table())
cur.execute(querys.create_light_table())
cur.execute(querys.insert_camera_data())
cur.execute(querys.insert_light_data())
cur.execute(querys.create_data_table("fir_data"))
cur.execute(querys.create_data_table("imgs_data"))
cur.execute(querys.create_score_table())
con.commit()


def camera_light_values(l):
    if l == ['logitech', 'fluorescente']:
        return '1','1'
    if l == ['logitech', 'halogeno']:
        return '1','2'
    if l == ['logitech', 'led']:
        return '1','3'
    if l == ['logitech', 'nir']:
        return '1','4'
    if l == ['microsoft', 'fluorescente']:
        return '2','1'
    if l == ['microsoft', 'halogeno']:
        return '2','2'
    if l == ['microsoft', 'led']:
        return '2','3'


def insert_data(file, table, connection, cursor, symbol=",", read_values=False):
    with open(file) as f:
        print("Leyendo " + file)
        lines = f.readlines()
        data = lines[1:]  # remove first 1 elements
        for line in data:
            l = line.replace("\n", "").split(symbol)
            if read_values:
                camera, light = camera_light_values(file.split("/")[-1].split("_")[0:2])
                frame = str(int(l[1].split("\\")[-1].split(".")[0].split("_")[-1]))
                l = l[:2] + [camera] + [light] + [frame] + l[2:]
            query = querys.generate_data_query(len(l), DB_NAME, table)
            try:
                cursor.execute(query, l)
                connection.commit()
            except Exception as e:
                print("Error en " + table)
                print(l)
                print(query)
                print("Error: " + str(e))
                con.rollback()


def insert_scores(file, table, connection, cursor, symbol=","):
    with open(file) as f:
        print("Leyendo " + file)
        lines = f.readlines()
        for line in lines:
            l = line.replace("\n", "").split(symbol)
            id_fir = int(l[0])
            id_img = int(l[2])
            score = float(l[4])
            camera, light = camera_light_values(file.split("/")[-1].split("_")[0:2])
            frame = str(int(l[3].split("\\")[-1].split(".")[0].split("_")[-1]))
            query = querys.generate_find_id_query(id=id_fir, table="fir_data", camera=1, light=1)
            cursor.execute(query)
            result = cursor.fetchone()
            id_fir_db = result[0]
            query = querys.generate_find_id_query(id=id_img, table="imgs_data", camera=camera, light=light, frame=frame)
            cursor.execute(query)
            result = cursor.fetchone()
            id_img_db = result[0]
            query = querys.insert_score_data(id_fir_db, id_img_db, score)
            cursor.execute(query)
            connection.commit()


# fir
print("Comenzamos la lectura de los fir.")
insert_data(FOLDER + "FIR/DATA/logitech_fluorescente_data.txt",
            "fir_data", con, cur)
insert_data(FOLDER + "FIR/DATA/logitech_halogeno_data.txt", "fir_data", con,
            cur)
insert_data(FOLDER + "FIR/DATA/logitech_led_data.txt", "fir_data", con, cur)
insert_data(FOLDER + "FIR/DATA/logitech_nir_data.txt", "fir_data", con, cur)
insert_data(FOLDER + "FIR/DATA/microsoft_fluorescente_data.txt",
            "fir_data", con, cur)
insert_data(FOLDER + "FIR/DATA/microsoft_halogeno_data.txt", "fir_data",
            con, cur)
insert_data(FOLDER + "FIR/DATA/microsoft_led_data.txt", "fir_data", con, cur)
print("----------------------------------------------------------")

# img data
print("Comenzamos la lectura de los img_data.")
insert_data(FOLDER + "DATA_INFO/DATA/logitech_fluorescente_imgs_data.csv",
            "imgs_data", con, cur, symbol=";", read_values=True)
insert_data(FOLDER + "DATA_INFO/DATA/logitech_halogeno_imgs_data.csv",
            "imgs_data", con, cur, symbol=";", read_values=True)
insert_data(FOLDER + "DATA_INFO/DATA/logitech_led_imgs_data.csv",
            "imgs_data", con, cur, symbol=";", read_values=True)
insert_data(FOLDER + "DATA_INFO/DATA/logitech_nir_imgs_data.csv",
            "imgs_data", con, cur, symbol=";", read_values=True)
insert_data(FOLDER + "DATA_INFO/DATA/microsoft_fluorescente_imgs_data.csv",
            "imgs_data", con, cur, symbol=";", read_values=True)
insert_data(FOLDER + "DATA_INFO/DATA/microsoft_halogeno_imgs_data.csv",
            "imgs_data", con, cur, symbol=";", read_values=True)
insert_data(FOLDER + "DATA_INFO/DATA/microsoft_led_imgs_data.csv",
            "imgs_data", con, cur, symbol=";", read_values=True)
print("----------------------------------------------------------")

#scores
print("Comenzamos la lectura de los scores.")
insert_scores(FOLDER + "SCORES/logitech_fluorescente_imgs_scores.txt", "score_data", con, cur)
insert_scores(FOLDER + "SCORES/logitech_halogeno_imgs_scores.txt", "score_data", con, cur)
insert_scores(FOLDER + "SCORES/logitech_led_imgs_scores.txt", "score_data", con, cur)
insert_scores(FOLDER + "SCORES/logitech_nir_imgs_scores.txt", "score_data", con, cur)
insert_scores(FOLDER + "SCORES/microsoft_fluorescente_imgs_scores.txt", "score_data", con, cur)
insert_scores(FOLDER + "SCORES/microsoft_halogeno_imgs_scores.txt", "score_data", con, cur)
insert_scores(FOLDER + "SCORES/microsoft_led_imgs_scores.txt", "score_data", con, cur)
print("----------------------------------------------------------")

# close con
con.close()

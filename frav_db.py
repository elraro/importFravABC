import MySQLdb as Mdb
import querys as querys
from collections import defaultdict
import dill

# Hardcoded
DB_HOST = ""
DB_USER = ""
DB_PASS = ""
DB_NAME = ""
FOLDER = ""

con = Mdb.connect(DB_HOST, DB_USER, DB_PASS, DB_NAME)
cur = con.cursor()

cur.execute(querys.create_camera_table())
cur.execute(querys.create_light_table())
cur.execute(querys.insert_camera_data())
cur.execute(querys.insert_light_data())
cur.execute(querys.create_data_table("pass_data"))
cur.execute(querys.create_data_table("imgs_data"))
cur.execute(querys.create_score_table())
con.commit()


def nested_dict(n, type):
    if n == 1:
        return defaultdict(type)
    else:
        return defaultdict(lambda: nested_dict(n-1, type))

fir_dict = nested_dict(4, int)
img_dict = nested_dict(4, int)


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


def insert_data(file, table, connection, cursor, count, symbol=",", dict_data=False):
    with open(file) as f:
        print("Leyendo " + file)
        lines = f.readlines()
        data = lines[1:]  # remove first 1 elements
        for line in data:
            l = line.replace("\n", "").split(symbol)
            camera, light = camera_light_values(file.split("/")[-1].split("_")[0:2])
            frame = str(int(l[1].split("\\")[-1].split(".")[0].split("_")[-1]))
            clase = str(int(l[0]))
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
            if dict_data:
                img_dict[clase][camera][light][frame] = count
            else:
                fir_dict[clase][camera][light][frame] = count
            # print(count)
            count += 1
    return count


def insert_scores(file, table, connection, cursor, symbol=","):
    with open(file) as f:
        print("Leyendo " + file)
        lines = f.readlines()
        temp = list()
        for line in lines:
            l = line.replace("\n", "").split(symbol)
            # print(l)
            id_class_fir = str(int(l[0]))
            id_class_img = str(int(l[2]))
            try:
                score = float(l[4])
            except ValueError as e:
                score = -1.0
            camera, light = camera_light_values(file.split("/")[-1].split("_")[0:2])
            frame = str(int(l[3].split("\\")[-1].split(".")[0].split("_")[-1]))
            # fir_dict[clase][camera][light][frame] = count
            id_fir_db = fir_dict[id_class_fir][camera][light]['0']
            id_img_db = img_dict[id_class_img][camera][light][frame]
            temp.append((id_fir_db, id_img_db, score))
            if len(temp) == 1000:
                try:
                    query = querys.insert_score_data(temp)
                    cursor.execute(query)
                    connection.commit()
                    temp.clear()
                except Exception as e:
                    print("Error en " + table)
                    print(l)
                    print(query)
                    print("Error: " + str(e))
                    con.rollback()
        if len(temp) != 0:
            try:
                query = querys.insert_score_data(temp)
                cursor.execute(query)
                connection.commit()
                temp.clear()
            except Exception as e:
                print("Error en " + table)
                print(l)
                print(query)
                print("Error: " + str(e))
                con.rollback()


# fir
print("Comenzamos la lectura de los fir.")
count = 1
count = insert_data(FOLDER + "FIR/DATA/logitech_fluorescente_data.txt", "pass_data", con, cur, count)
count = insert_data(FOLDER + "FIR/DATA/logitech_halogeno_data.txt", "pass_data", con, cur, count)
count = insert_data(FOLDER + "FIR/DATA/logitech_led_data.txt", "pass_data", con, cur, count)
count = insert_data(FOLDER + "FIR/DATA/logitech_nir_data.txt", "pass_data", con, cur, count)
count = insert_data(FOLDER + "FIR/DATA/microsoft_fluorescente_data.txt", "pass_data", con, cur, count)
count = insert_data(FOLDER + "FIR/DATA/microsoft_halogeno_data.txt", "pass_data", con, cur, count)
count = insert_data(FOLDER + "FIR/DATA/microsoft_led_data.txt", "pass_data", con, cur, count)
print("----------------------------------------------------------")

# img data
print("Comenzamos la lectura de los img_data.")
count = 1
count = insert_data(FOLDER + "DATA_INFO/DATA/logitech_fluorescente_imgs_data.csv",
            "imgs_data", con, cur, count, symbol=";", dict_data=True)
count = insert_data(FOLDER + "DATA_INFO/DATA/logitech_halogeno_imgs_data.csv",
            "imgs_data", con, cur, count, symbol=";", dict_data=True)
count = insert_data(FOLDER + "DATA_INFO/DATA/logitech_led_imgs_data.csv",
            "imgs_data", con, cur, count, symbol=";", dict_data=True)
count = insert_data(FOLDER + "DATA_INFO/DATA/logitech_nir_imgs_data.csv",
            "imgs_data", con, cur, count, symbol=";", dict_data=True)
count = insert_data(FOLDER + "DATA_INFO/DATA/microsoft_fluorescente_imgs_data.csv",
            "imgs_data", con, cur, count, symbol=";", dict_data=True)
count = insert_data(FOLDER + "DATA_INFO/DATA/microsoft_halogeno_imgs_data.csv",
            "imgs_data", con, cur, count, symbol=";", dict_data=True)
count = insert_data(FOLDER + "DATA_INFO/DATA/microsoft_led_imgs_data.csv",
            "imgs_data", con, cur, count, symbol=";", dict_data=True)
print("----------------------------------------------------------")


# dump
print("Vamos a guardar los diccionarios con los id de la bbdd")
dill.dump(fir_dict, open("fir_dict.bin", "wb"))
dill.dump(img_dict, open("img_dict.bin", "wb"))
print("----------------------------------------------------------")


# lectura de los dump
# para no tener que reconstruir de nuevo los dict, los he dumpeado
fir_dict = dill.load(open("fir_dict.bin", "rb"))
img_dict = dill.load(open("img_dict.bin", "rb"))


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

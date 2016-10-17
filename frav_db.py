import MySQLdb as Mdb
import querys as querys

# Hardcoded
DB_HOST = "localhost"
DB_USER = "frav"
DB_PASS = "VXxL4UOLvB6wc01Y3Cxi"
DB_NAME = "frav_ABC"
FOLDER = "/media/alberto/Datos/FRAV_ALBERTO/"

con = Mdb.connect(DB_HOST, DB_USER, DB_PASS, DB_NAME)
cur = con.cursor()

# cur.execute(querys.create_camera_table())
# cur.execute(querys.create_light_table())
# cur.execute(querys.insert_camera_data())
# cur.execute(querys.insert_light_data())
# cur.execute(querys.create_data_table("fir_data"))
# cur.execute(querys.create_data_table("imgs_data"))
# con.commit()


def insert_data(file, table, connection, cursor, symbol=","):
    with open(file) as f:
        print("Leyendo " + file)
        lines = f.readlines()
        data = lines[1:]  # remove first 1 elements
        for line in data:
            l = line.replace("\n", "").split(symbol)
            query = querys.generate_query(len(l), DB_NAME, table)
            try:
                cursor.execute(query, l)
                connection.commit()
            except Exception as e:
                print("Error en " + table)
                print(l)
                print(query)
                print("Error: " + str(e))
                con.rollback()


# fir
# insert_data(FOLDER + "FIR/DATA/logitech_fluorescente_data.txt",
#             "fir_data", con, cur)
# insert_data(FOLDER + "FIR/DATA/logitech_halogeno_data.txt", "fir_data", con,
#             cur)
# insert_data(FOLDER + "FIR/DATA/logitech_led_data.txt", "fir_data", con, cur)
# insert_data(FOLDER + "FIR/DATA/logitech_nir_data.txt", "fir_data", con, cur)
# insert_data(FOLDER + "FIR/DATA/microsoft_fluorescente_data.txt",
#             "fir_data", con, cur)
# insert_data(FOLDER + "FIR/DATA/microsoft_halogeno_data.txt", "fir_data",
#             con, cur)
# insert_data(FOLDER + "FIR/DATA/microsoft_led_data.txt", "fir_data", con, cur)

# img data
insert_data(FOLDER + "DATA_INFO/DATA/logitech_fluorescente_imgs_data.csv",
            "imgs_data", con, cur, ";")
insert_data(FOLDER + "DATA_INFO/DATA/logitech_halogeno_imgs_data.csv",
            "imgs_data", con, cur, ";")
insert_data(FOLDER + "DATA_INFO/DATA/logitech_led_imgs_data.csv",
            "imgs_data", con, cur, ";")
insert_data(FOLDER + "DATA_INFO/DATA/logitech_nir_imgs_data.csv",
            "imgs_data", con, cur, ";")
insert_data(FOLDER + "DATA_INFO/DATA/microsoft_fluorescente_imgs_data.csv",
            "imgs_data", con, cur, ";")
insert_data(FOLDER + "DATA_INFO/DATA/microsoft_halogeno_imgs_data.csv",
            "imgs_data", con, cur, ";")
insert_data(FOLDER + "DATA_INFO/DATA/microsoft_led_imgs_data.csv",
            "imgs_data", con, cur, ";")

#scores
# TODO

# close con
con.close()

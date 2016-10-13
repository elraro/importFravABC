import MySQLdb as Mdb
import querys as querys

# Hardcoded
DB_HOST = "localhost"
DB_USER = "frav"
DB_PASS = "VXxL4UOLvB6wc01Y3Cxi"
DB_NAME = "frav_ABC"

con = Mdb.connect(DB_HOST, DB_USER, DB_PASS, DB_NAME)
cur = con.cursor()

cur.execute(querys.create_table("fir_logitech_fluorescente_data"))
cur.execute(querys.create_table("fir_logitech_halogeno_data"))
cur.execute(querys.create_table("fir_logitech_led_data"))
cur.execute(querys.create_table("fir_logitech_nir_data"))
cur.execute(querys.create_table("fir_microsoft_fluorescente_data"))
cur.execute(querys.create_table("fir_microsoft_halogeno_data"))
cur.execute(querys.create_table("fir_microsoft_led_data"))
cur.execute(querys.create_table("imgs_logitech_fluorescente_data"))
cur.execute(querys.create_table("imgs_logitech_halogeno_data"))
cur.execute(querys.create_table("imgs_logitech_led_data"))
cur.execute(querys.create_table("imgs_logitech_nir_data"))
cur.execute(querys.create_table("imgs_microsoft_fluorescente_data"))
cur.execute(querys.create_table("imgs_microsoft_halogeno_data"))
cur.execute(querys.create_table("imgs_microsoft_led_data"))
con.commit()


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


insert_data("/media/alberto/Datos/FRAV_ALBERTO/FIR/DATA/logitech_fluorescente_data.txt",
            "fir_logitech_fluorescente_data", con, cur)
insert_data("/media/alberto/Datos/FRAV_ALBERTO/FIR/DATA/logitech_halogeno_data.txt", "fir_logitech_halogeno_data", con,
            cur)
insert_data("/media/alberto/Datos/FRAV_ALBERTO/FIR/DATA/logitech_led_data.txt", "fir_logitech_led_data", con, cur)
insert_data("/media/alberto/Datos/FRAV_ALBERTO/FIR/DATA/logitech_nir_data.txt", "fir_logitech_nir_data", con, cur)
insert_data("/media/alberto/Datos/FRAV_ALBERTO/FIR/DATA/microsoft_fluorescente_data.txt",
            "fir_microsoft_fluorescente_data", con, cur)
insert_data("/media/alberto/Datos/FRAV_ALBERTO/FIR/DATA/microsoft_halogeno_data.txt", "fir_microsoft_halogeno_data",
            con, cur)
insert_data("/media/alberto/Datos/FRAV_ALBERTO/FIR/DATA/microsoft_led_data.txt", "fir_microsoft_led_data", con, cur)

insert_data("/media/alberto/Datos/FRAV_ALBERTO/DATA_INFO/DATA/logitech_fluorescente_imgs_data_CORREGIDO.csv",
            "imgs_logitech_fluorescente_data", con, cur, ";")
insert_data("/media/alberto/Datos/FRAV_ALBERTO/DATA_INFO/DATA/logitech_halogeno_imgs_data_CORREGIDO.csv",
            "imgs_logitech_halogeno_data", con, cur, ";")
insert_data("/media/alberto/Datos/FRAV_ALBERTO/DATA_INFO/DATA/logitech_led_imgs_data_CORREGIDO.csv",
            "imgs_logitech_led_data", con, cur, ";")
insert_data("/media/alberto/Datos/FRAV_ALBERTO/DATA_INFO/DATA/logitech_nir_imgs_data_CORREGIDO.csv",
            "imgs_logitech_nir_data", con, cur, ";")
insert_data("/media/alberto/Datos/FRAV_ALBERTO/DATA_INFO/DATA/microsoft_fluorescente_imgs_data_CORREGIDO.csv",
            "imgs_microsoft_fluorescente_data", con, cur, ";")
insert_data("/media/alberto/Datos/FRAV_ALBERTO/DATA_INFO/DATA/microsoft_halogeno_imgs_data_CORREGIDO.csv",
            "imgs_microsoft_halogeno_data", con, cur, ";")
insert_data("/media/alberto/Datos/FRAV_ALBERTO/DATA_INFO/DATA/microsoft_led_imgs_data_CORREGIDO.csv",
            "imgs_microsoft_led_data", con, cur, ";")
con.close()

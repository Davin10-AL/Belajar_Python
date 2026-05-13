from . import Operasi    


DB_NAME = "data.txt"
TEMPLATE = {
    "pk":"XXXXXX",
    "date_add":"yyyy-mm-dd",
    "judul":255*" ",
    "penulis":255*" ",
    "tahun":"yyyy",
}

def init_console():
    try:
        with open(DB_NAME,'r')as file:
            print("Database tersedia, init done!")
    except:
        print(f"Database tidak ditemukan")
        # with open(DB_NAME,'w',encoding="utf-8")as file:
        #     penulis = input(f"Penulis: ")
        #     judul = input(f"Judul: ") 
        #     tahun = input(f"Tahun: ")
        #     # data_str = f"{penulis},{tahun},{judul}"
        #     file.write(data_str)
        Operasi.create_first_data()
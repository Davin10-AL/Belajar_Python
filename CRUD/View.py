from . import Operasi

def delete_console():
    read_console()
    while(True):
        print("silahkan pilih No buku yang akan didelete:")
        no_buku = int(input("Nomor Buku: "))
        data_buku = Operasi.read(index=no_buku)

        if data_buku:
            data_break = data_buku.split(',')
            pk = data_break[0]
            data_add = data_break[1]
            penulis = data_break[2]
            judul = data_break[3]
            tahun = data_break[4][:-1]

            # data yang mau dihapus
            print("\n" + "="*100)
            print("Data yang ingin anda Delete")
            print(f"1. Judul\t: {judul:.40}")
            print(f"2. Penulis\t: {penulis:.40}")
            print(f"3. Tahun\t: {tahun:.4}")
            is_done = input(f"Apakah anda yakin (y/n)? ")
            if is_done == "y" or is_done == "Y":
                Operasi.delete(no_buku)
                break
        else:
            print("Nomor tidak valid, silahkan masukkan lagi")

    print("Data Berhasil dihapus!")


def update_console():
    read_console()
    while(True):
        print("silahkan pilih No buku yang akan diupdate:")
        no_buku = int(input("Nomor Buku: "))
        data_buku = Operasi.read(index=no_buku)

        if data_buku:
            break
        else:
            print("Nomor tidak valid, silahkan masukkan lagi")

    data_break = data_buku.split(',')
    pk = data_break[0]
    data_add = data_break[1]
    penulis = data_break[2]
    judul = data_break[3]
    tahun = data_break[4][:-1]

    # print(pk)
    # print(data_add)
    # print(penulis)
    # print(judul)
    # print(tahun)

    while(True):
        # data yang mau diupdate
        print("\n" + "="*100)
        print("silahkan pilih data yang akan diubah")
        print(f"1. Judul\t: {judul:.40}")
        print(f"2. Penulis\t: {penulis:.40}")
        print(f"3. Tahun\t: {tahun:.4}")

        # memiilih mode untuk update
        user_option = input("pilih data [1,2,3]: ")
        print("\n" + "="*100)
        match user_option:
            case "1" :judul = input("judul\t: ") 
            case "2" :penulis = input("penulis\t: ") 
            case "3" :
                while(True): # loop untuk penulisan tahun
                    try:
                        tahun = int(input("Tahun\t: "))
                        if len(str(tahun)) == 4: # untuk membuat tahun hanya bisa diketik 4 aja
                            break
                        else:
                            print(f"Tahun harus angka, silahkan masukkan lagi! (yyyy)")

                    except:
                        print(f"Tahun harus angka, silahkan masukkan lagi! (yyyy)")
            case _: print("index tidak cocok")

        print("Data Baru")
        print(f"1. Judul\t: {judul:.40}")
        print(f"2. Penulis\t: {penulis:.40}")
        print(f"3. Tahun\t: {tahun:4}")
        is_done = input(f"Apakah data sudah sesuai(y/n)? ")
        if is_done == "y" or is_done == "Y":
            break

    Operasi.update(no_buku,pk,data_add,tahun,judul,penulis)

def create_console():
    print("\n" + "="*100)
    print("silahkan tambah data buku\n")
    penulis = input("Penulis\t: ")
    judul = input("Judul\t: ")
    while(True): # loop untuk penulisan tahun
        try:
            tahun = int(input("Tahun\t: "))
            if len(str(tahun)) == 4: # untuk membuat tahun hanya bisa diketik 4 aja
                break
            else:
                print(f"Tahun harus angka, silahkan masukkan lagi! (yyyy)")

        except:
            print(f"Tahun harus angka, silahkan masukkan lagi! (yyyy)")

    Operasi.create(tahun,judul,penulis)
    print(f"\nBerikut adalah data baru!")
    read_console()



def read_console():
    data_file = Operasi.read()

    index = "No"
    judul = "Judul"
    penulis = "Penulis"
    tahun = "Tahun"

    # Header
    print("\n" + "="*100)
    print(f"{index:4} | {judul:40} | {penulis:40} | {tahun:5}")
    print(f"{"-"*100}")

    # Data
    for index,data in enumerate(data_file):
        data_break = data.split(",")
        
        # print(data_break)
        pk = data_break[0]
        date_add = data_break[1]
        penulis = data_break[2]
        judul = data_break[3]
        tahun = data_break[4]
        print(f"{index+1:4} | {judul:40} | {penulis:40} | {tahun:4}",end="")

    # Footer
    print("="*100+"\n")
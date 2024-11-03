#management
import data  # type: ignore
import inputs, ui # type: ignore

'''==================== F13 - Monster Management ===================='''
monster = []

def update_data():
    global monster
    monster = data.monster

def simpan_data():
    global monster
    data.monster = monster

def monster_admin():
    update_data()
    ui.border("SELAMAT DATANG DI DATABASE PARA MONSTER!!!")
    print()
    print("1. Tampilkan semua Monster")
    print("2. Tambah Monster baru")
    print("3. Kembali ke menu utama")
    print()

    choice = input("Pilih Aksi: ")
    while (not inputs.is_in_range(choice, 1, 3)):
        choice = input("Pilih Aksi: ")

    choice = int(choice)

    if(choice == 3): #kembali ke menu utama
        return

    while(choice != 3):
        if(choice == 1):
            tampilkan_monster()
        elif(choice == 2):
            tambah_monster()
        
        choice = input("Pilih Aksi: ")
        while (not inputs.is_in_range(choice, 1, 3)):
            choice = input("Pilih Aksi: ")

        choice = int(choice)

    simpan_data()

def tampilkan_monster():
        update_data()
        headers = ["ID", "Type", "ATK Power", "Def Power", "HP"]
        ui.table(headers, monster)
        simpan_data()

def tambah_monster():
    update_data()
    
    nama = input("Masukkan Type / Nama : ")
    while(tersedia(nama)):
        print("Nama sudah terdaftar, coba lagi!")
        print()
        nama = input("Masukkan Type / Nama : ")
    
    atk = input("Masukkan ATK Power: ")
    while(not inputs.is_number(atk) or not inputs.is_positif(atk)):
        if(not inputs.is_number(atk)) :
            print("Masukkan input bertipe Integer, coba lagi!")
            print()
        else:
            print("Masukkan input harus postif")
            print()
        atk = input("Masukkan ATK Power: ")
        

    def_pw = input("Masukkan DEF Power: ") #pastikan apakah masukkan def power ini sudah pasti integer?

    while(not inputs.is_number(def_pw) or not cek_range(int(def_pw))):
        if(not inputs.is_number(def_pw)):
            print("Masukkan input bertipe Integer, coba lagi!")
            print()
        else:
            print("DEF Power harus bernilai 0-50, coba lagi!")
            print()

        def_pw = input("Masukkan DEF Power: ")

    hp = input("Masukkan HP: ")
    while(not inputs.is_number(hp) or not inputs.is_positif(hp)):
        if(not inputs.is_number(hp)) :
            print("Masukkan input bertipe Integer, coba lagi!")
            print()
        else:
            print("Masukkan input harus postif")
            print()

        hp = input("Masukkan HP: ")

    hp = int(hp)

    ui.border(f'''
{ui.monster1}
Monster baru berhasil dibuat!!!!
===================================
Type : {nama}
ATK Power : {atk}
DEF Power : {def_pw}
HP : {hp}
===================================
''')

    y_n = input("Tambahkan Monster ke Database(Y/N): ")
    while (y_n.upper() != "Y" and y_n.upper() != "N"):
        y_n = input("Tambahkan Monster ke Database(Y/N): ")

    if(y_n.upper() == "Y"):
        tmp = []
        tmp.append(int(monster[len(monster)-1][0]) + 1)
        tmp.append(nama)
        tmp.append(atk)
        tmp.append(def_pw)
        tmp.append(hp)
        monster.append(tmp)
        print("Monster baru telah ditambahkan!")
        print()

    else:
        print("Monster gagal ditambahkan!")
        print()
    
    simpan_data()

def tersedia(c):
    global monster
    for i in range (1, len(monster)):
        if (c == monster[i][1]):
            return True
    return False

def cek_range(x):
    return (0 <= x and x <= 50)

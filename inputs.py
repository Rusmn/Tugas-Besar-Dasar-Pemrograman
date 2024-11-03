import data # type: ignore
import ui # type: ignore

user = [] #[x][0] : id, [x][1] = user, [x][2] = pass, [x][3] = role, [x][4] = pass
monster = [] #[x][0] : id, [x][1] = type, [x][2] = atk_power, [x][3] = def_power, [x][4] = hp
monster_inven = []
cek_login = True
nama = " "
id = 0

def update_data():
    global user, monster, monster_inven

    user = data.user
    monster = data.monster
    monster_inven = data.monster_inven

def simpan_data():
    global user, monster, monster_inven

    data.user = user
    data.monster = monster
    data.monster_inven = monster_inven

def validasi(c):
    cek = 0
    for i in range (len(c)):
        if((65 <= ord(c[i]) and ord(c[i]) <= 90) or (97 <= ord(c[i]) and ord(c[i]) <= 122) or (48 <= ord(c[i]) and ord(c[i]) <= 57) or c[i] == "-" or c[i] == "_"):
            cek+= 1
    if cek == len(c): 
        return True
    else:
        return False

def full_int(x): #cek apakah full angka atau tidak
    cek = True
    for i in x:
        if not is_number(i):
            cek = cek and False
    return cek

def is_number(x):
    for i in x:
        if(ord(i) == ord('-')) : i = '0'
        if not (ord('0') <= ord(i) <= ord('9')):
            return False
        return True
    
def is_positif(x):
    x = int(x)
    return x >= 0
              
def tersedia_username(c):
    global user
    for i in range(1, len(user)):
        if(user[i][1] == c):
            return True
    return False 

def is_in_range(x, awal, akhir):
    cek = True
    if (x == ''):
        print("Input kosong, masukkan input yang tepat!!!")
        return False
    elif(full_int(x)):
        x = int(x)
        if(awal > x or x > akhir):
            print("Data tidak ada, silahkan pilih yang tertera.")
            cek = False
        return cek
    else:
        print("Masukkan harus angka!!!")
        return False
    

'''==================== F01 - Register ==================== '''

def regis():
    global nama, id, cek_login, user, monster_inven
    update_data()
    tmp_regis = []
    tmp_monster = []

    print("[Untuk membatalkan registrasi, kosongkan username dengan menekan ENTER]")
    username = input("Masukkan username baru: ")
    print()

    if(username == ''):
        print("Register dibatalkan!!")
        print()
        return
    
    #validasi username sesuai syarat (terdiri dari a-z, A-Z, 0-9, '_', '-') dan mengecek ketersediaan username
    while(not validasi(username) or tersedia_username(username)):
        if(not validasi(username)):
            print("Username hanya boleh berisi alfabet, angka, underscore, dan strip!")
        elif(tersedia_username(username)):
            print(f"Username {username} sudah terpakai, silahkan gunakan username lain!")
        print("[Untuk membatalkan registrasi, kosongkan username lalu tekan ENTER]")
        username = input("Masukkan username baru: ")
        print()
        if(username == ''):
            print("Register dibatalkan!!")
            print()
            return
    
    password = input("Masukkan password: ")
    
    tmp_regis.append(len(user)) #id dibuat baru
    tmp_regis.append(username)
    tmp_regis.append(password)
    tmp_regis.append("agent") #setiap user baru adalah admin
    tmp_regis.append(0) #owca untuk tiap user baru sama dengan 0, sesuai ketentuan spek

    user.append(tmp_regis)
    
    print("Silakan pilih monster untuk menemani awal perjalananmu!") #pilihan monster dibatasi hanya 5 monster saja
    for i in range(1,6):
        print(monster[i][0] + ". " + monster[i][1])

    pilihan = input("Monster Pilihan: ")
    
    while (not is_in_range(pilihan, 1, 5)):
        pilihan = input("Monster Pilihan: ")

    #perhatikan bagian in, data tidak berlaku umum, cuman untuk folder data_base
    tmp_monster.append(len(user)-1)
    tmp_monster.append(int(pilihan))
    tmp_monster.append(1)

    monster_inven.append(tmp_monster)

    cek_login = False

    ui.border (f'''
                    Registrasi berhasil. Sekarang anda sudah login.
               
Selamat datang Agent {username}. Mari kita mengalahkan Dr. Asep Spakbor dengan {monster[int(pilihan)][1]}!''')
    
    nama = username
    id = int(user[len(user)-1][0])

    simpan_data()
    print(data.monster_inven)



''' ==================== F02-Login ===================='''
def login():
    update_data()
    global nama, id
    global cek_login
    global user

    print("[Untuk membatalkan login, kosongkan username dan password dengan menekan ENTER dua kali]")
    username = input("Masukkan username: ")
    password = input("Masukkan password: ")
    print()

    if(username == '' and password == ''):
        return

    nama = username
    cek_user = False
    cek_pass = False 

    for i in range (len(user)):
        if(username == user[i][1]):
            id = int(user[i][0])
            cek_user = True
            break
    
    for i in range (len(user)):
        if(password == user[i][2]):
            cek_pass = True
            break

    if(cek_user and cek_pass):
        print(f"Login berhasil, selamat datang {username}!")
        print()
        cek_login = False
    else :
        print("Username atau password salah. Silakan coba lagi.")
        print()
        login()
    
    simpan_data()


''' ==================== F03 - Logout ===================='''

def logout():
    update_data()
    global cek_login
    global nama

    if (not cek_login):
        print(f"Logout berhasil, {nama} telah keluar.")
        cek_login = True
    else :
        print("Logout gagal!")
        print("Anda belum login, silahkan login terlebih dahulu sebelum melakukan logout")

    







    


    


    

    

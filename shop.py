import data, utility  # type: ignore
import inputs, ui # type: ignore

'''
TO DO :
1. PERBAIKI TAMPILAN UI
2. EFISIENSIKAN KODE DENGAN SUBPROGRAM (HAPUS,LIHAT,UBAH,TAMBAH)
3. URUTKAN DATA TIAP ADA PERUBAHAN BERDASARKAN ID
'''

'''==================== F12 - Shop Management ===================='''

monster = []
dm = []
di =[]
monster_inven = []
potion = [[0,"None"] , [1,"strength"] , [2,"resilience"] , [3,"healing"]]
item = []

def update_data():
    global monster, dm, di, monster_inven, item
    monster = data.monster
    dm = data.monster_shop
    di = data.stuff
    monster_inven = data.monster
    item = data.item


def simpan_data():
    global monster, dm, di, monster_inven, item
    data.monster = monster
    data.monster_shop = dm
    data.stuff = di
    data.monster_inven = monster_inven
    data.item = item

def shop_admin():
    aksi = ["lihat", "tambah", "ubah" , "hapus", "keluar"]
    choice = input("Pilih aksi (lihat/tambah/ubah/hapus/keluar): ")

    while (choice.lower() not in aksi):
        choice = input("Pilih aksi (lihat/tambah/ubah/hapus/keluar): ")
    
    while(choice.lower() != "keluar"):
        if (choice.lower() == "lihat"):
            shop_lihat()
        elif (choice.lower() == "tambah"):
            shop_tambah()
        elif (choice.lower() == "ubah"):
            shop_ubah()
        elif (choice.lower() == "hapus"):
            shop_hapus()

        choice = input("Pilih aksi (lihat/tambah/ubah/hapus/keluar): ")
    
    ui.border("TERIMAAA KASIIIHHH!!!!")

def pilihan(s):
    choice = input(f"Mau {s} apa? (monster/potion): ")
    while (choice.lower() != "monster" and choice.lower() != "potion"):
        choice = input(f"Mau {s} apa? (monster/potion): ")
    return choice

def tampilkan_monster():
    ui.border("MONSTER")
    print()
    headers = ["ID", "Type", "ATK Power", "DEF Power" ,"HP" ,"Stok", "Harga"]
    ui.table(headers,dm)
    print()

def tampilkan_item():
    ui.border("POTION")
    print()
    print("ID \t Type    \t Stok \t Harga")
    print("=======================================")
    for i in range (1, len(di)):
        print(f"{i} \t {di[i][0]} \t {di[i][1]} \t {di[i][2]}")
    print()

def shop_lihat():
    s = "lihat"
    update_data()
    choice = pilihan(s)
    if(choice.lower() == "monster"):
        tampilkan_monster()
    elif(choice.lower() == "potion"):
        tampilkan_item()

def shop_tambah():
    s ="nambahin"
    update_data()
    choice = pilihan(s)

    if(choice == "monster"):
        tmp1 = [] #tm = temporary array
        tmp2 = [] 
        tmp3 = []

        temporarry_arr(tmp1, tmp2, monster, dm)

        tmp1 = [int(x) for x in tmp1]

        header = ["ID", "Type", "ATK Power", "DEF Power", "HP"]
        tmp3.append(header)
        for i in range (len(tmp1)):
            tmp = []
            tmp.append(monster[tmp1[i]][0])
            tmp.append(monster[tmp1[i]][1])
            tmp.append(monster[tmp1[i]][2])
            tmp.append(monster[tmp1[i]][3])
            tmp.append(monster[tmp1[i]][4])
            tmp3.append(tmp)

        ui.table(header, tmp3)
        print()

        id = input("Masukkan id monster: ")
        while(not inputs.is_in_range(id, int(tmp3[1][0]), int(tmp3[len(tmp3)-1][0]))):
            id = input("Masukkan id monster: ")

        id = int(id)

        stok = input("Masukkan stok awal: ")
        while(not inputs.is_number(stok)):
            print("Masukkan hanya berupa angka!")
            stok = input("Masukkan stok awal: ")
        
        stok = int(stok)

        harga = input("Masukkan harga awal: ")
        while(not inputs.is_number(harga)):
            print("Masukkan hanya berupa angka!")
            harga = input("Masukkan harga awal: ")

        harga = int(harga)

        tambah_item(id, stok, harga, dm)

        ui.border(f"{monster[id][1]} telah berhasil ditambahkan ke dalam shop!" )
        print()
        
    else: 
        tmp1 = [] 
        tmp2 = []
        tmp3 = []
        tmp_potion =[]

        for i in range(len(di)):
            tmp = []
            tmp.append(i)
            tmp.append(di[i][0])
            tmp.append(di[i][1])
            tmp.append(di[i][2])
            tmp_potion.append(tmp)
        
        temporarry_arr(tmp1,tmp2, potion, tmp_potion)

        tmp1 = [int(x) for x in tmp1]

        header = ["ID", "Type"]
        tmp3.append(header)

        for i in range(len(tmp1)):
            tmp = []
            tmp.append(potion[tmp1[i]][0])
            tmp.append(potion[tmp1[i]][1])
            tmp3.append(tmp)

        ui.table(header, tmp3)
        print()

        id = input("Masukkan id potion: ")
        while(not inputs.is_in_range(id, int(tmp3[1][0]), int(tmp3[len(tmp3)-1][0]))):
            id = input("Masukkan id potion: ")

        id = int(id)

        stok = input("Masukkan stok awal: ")
        while(not inputs.is_number(stok)):
            print("Masukkan hanya berupa angka!")
            stok = input("Masukkan stok awal: ")
        
        stok = int(stok)

        harga = input("Masukkan harga awal: ")
        while(not inputs.is_number(harga)):
            print("Masukkan hanya berupa angka!")
            harga = input("Masukkan harga awal: ")

        harga = int(harga)

        tambah_item(id, stok, harga, di)

        ui.border(f"{potion[id][1]} telah berhasil ditambahkan ke dalam shop!" )
        print()


def tambah_item(id, stok, harga, arr):
    tmp = []
    if(arr == dm):
        tmp.append(id)
        tmp.append(monster[id][1])
        tmp.append(monster[id][2])
        tmp.append(monster[id][3])
        tmp.append(monster[id][4])
    else:
        tmp.append(potion[id][1])
    tmp.append(stok)
    tmp.append(harga)

    arr.append(tmp)
    simpan_data()

def temporarry_arr(tmp1, tmp2, data1, data2):
    for i in range(len(data2)):
        tmp2.append(data2[i][1])
    for i in range (1, len(data1)):
        if(data1[i][1] not in tmp2):
            tmp1.append(data1[i][0])
    tmp1 = [int(x) for x in tmp1]

def ubah_int(s):
    character = ' \n\t'
    if(s in character):
        return 0
    else:
        a = int(s)
        return a

def shop_ubah():
    s = "ubah"
    choice = pilihan(s)
    update_data()

    if (choice == "monster"):
        tampilkan_monster()
        id = int(input("Masukkan id monster: "))
        stok = input("Masukkan stok baru: ")
        harga = input("Masukkan harga baru: ")

        stok = ubah_int(stok)
        harga = ubah_int(harga)

        if(stok == 0):
            dm[id][6] = harga
        elif (harga == 0):
            dm[id][5] = stok
        else:
            dm[id][5] = stok
            dm[id][6] = harga

        if(stok == 0):
            ui.border(f"{dm[id][1]} telah berhasil diubah dengan harga baru {harga}!")
            print()
        elif (harga == 0):
            ui.border(f"{dm[id][1]} telah berhasil diubah dengan stok baru sejumlah {stok}!")
            print()
        else:
            ui.border(f"{dm[id][1]} telah berhasil diubah dengan stok baru sejumlah {stok} dan dengan harga baru {harga}!")
            print()

    else:
        tampilkan_item()
        id = int(input("Masukkan id potion: "))
        stok = input("Masukkan stok baru: ")
        harga = input("Masukkan harga baru: ")

        stok = ubah_int(stok)
        harga = ubah_int(harga)

        if(stok == 0):
            di[id][2] = harga
        elif (harga == 0):
            di[id][1] = stok
        else:
            di[id][1] = stok
            di[id][2] = harga

        if(stok == 0):
            ui.border(f"{di[id][0]} telah berhasil diubah dengan harga baru {harga}!")
            print()
        elif (harga == 0):
            ui.border(f"{di[id][0]} telah berhasil diubah dengan stok baru sejumlah {stok}!")
            print()
        else:
            ui.border(f"{di[id][0]} telah berhasil diubah dengan stok baru sejumlah {stok} dan dengan harga baru {harga}!")
            print()
    
    simpan_data() 

def cari_idx(x, data): 

    for i in range(1, len(data)):
        if(x == int(data[i][0])):
            return i
    return 0

def shop_hapus():
    s = "hapus"
    update_data()
    choice = pilihan(s)

    if(choice == "monster"):
        tampilkan_monster()
        id = int(input("Masukkan id monster: "))
        idx = cari_idx(id, dm)

        y_n = input(f"Apakah anda yakin ingin menghapus {dm[idx][1]} dari shop (y/n)? ")

        if(y_n == "y"):
            ui.border(f"{dm[idx][1]} telah berhasil dihapus dari shop!")
            print()
            tmp = utility.del_idx(dm, idx)
            data.monster_shop = tmp
        else:
            ui.border("Penghapusan dibatalkan")
            print()
    
    else:
        tampilkan_item()
        id = int(input("Masukkan id potion: "))

        tmp_potion = []

        for i in range(len(di)):
            tmp = []
            tmp.append(i)
            tmp.append(di[i][0])
            tmp.append(di[i][1])
            tmp.append(di[i][2])
            tmp_potion.append(tmp)

        idx = cari_idx(id, tmp_potion)

        y_n = input(f"Apakah anda yakin ingin menghapus {di[idx][0]} dari shop (y/n)? ")

        if(y_n == "y"):
            ui.border(f"{di[idx][0]} telah berhasil dihapus dari shop!")
            print()
            tmp = utility.del_idx(di, idx)
            data.stuff = tmp
        else:
            ui.border("Penghapusan dibatalkan")
            print()
    
    
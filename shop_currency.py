import data, os  # type: ignore

dm = []
di = []
potion = [[0,"None"] , [1,"strength"] , [2,"resilience"] , [3,"healing"]]

folder_name = 'data'

def update_data():
    global dm,di
    dm = data.monster_shop
    di = data.stuff

def get_user_oc(id, user):
    for i in range(1, len(user)):
        if user[i][0] == str(id):
            return int(user[i][4])
    return 0

tmp_potion = []

def isi_potion():
    global tmp_potion
    update_data()

    for i in range(len(di)):
        tmp = []
        tmp.append(i)
        tmp.append(di[i][0])
        tmp.append(di[i][1])
        tmp.append(di[i][2])
        tmp_potion.append(tmp)

def tampilkan_monster():
    update_data()
    print("ID \t | \t Type \t\t | ATK Power \t | Def Power \t | \t HP \t | \t Stok \t | \t Harga")
    for i in range (1, len(dm)):
        print(f"{dm [i][0]} \t | \t {dm[i][1]} \t | \t {dm[i][2]} \t | \t {dm[i][3]} \t | \t {dm[i][4]} \t | \t {dm[i][5]} \t | \t {dm[i][6]}" )


def tampilkan_item():
    global tmp_potion
    print("ID \t | Type \t | \t Stok \t | \t Harga")
    for i in range (1, len(tmp_potion)):
        print(f"{tmp_potion[i][0]} \t | {tmp_potion[i][1]} \t | \t {tmp_potion[i][2]} \t | \t {tmp_potion[i][3]}")

def shopcurrency(user_id):
    global folder_name, tmp_potion
    update_data()
    user = data.user
    oc_user = get_user_oc(user_id, user)
    monster_shop = data.monster_shop
    item_shop = data.stuff
    monster_inventory = data.monster_inven
    isi_potion()

    print("Selamat datang di SHOP!!! Pastikan O.W.C.A mu cukup ya !!! (^ w ^)")
    
    while True: 
        choice = input("Pilih aksi (lihat/beli/keluar) : ")

        if choice == "lihat":
            item_type = input("Mau lihat apa??? (monster/potion): ")
            if item_type == 'monster':
                print("Monster Shop:")
                update_data()
                tampilkan_monster()

            elif item_type == 'potion':
                print("Potion Shop:")
                update_data()
                tampilkan_item()

            else:
                print("Silakan pilih antara 'monster' atau 'potion' !")

        elif choice ==  "beli":
            print(f"Jumlah O.W.C.A mu sekarang adalah {oc_user} OC.")

            valid_item_types = ['monster', 'potion']
            item_type = input("Mau beli apa??? (monster/potion): ")

            valid_ids = []

            while item_type not in valid_item_types:
                print("Input tidak valid. Silakan pilih ulang.")
                item_type = input("Mau beli apa??? (monster/potion): ")

            for i in range(len(di)):
                tmp = []
                tmp.append(i)
                tmp.append(item_shop[i][0])
                tmp.append(item_shop[i][1])
                tmp.append(item_shop[i][2])
                tmp_potion.append(tmp)

            if item_type == 'monster':
                valid_ids = [row[0] for row in monster_shop]
            elif item_type == 'potion':
                valid_ids = [row[0] for row in tmp_potion]

            item_id = int(input("Masukkan ID yang mau kamu beli : "))

            if str(item_id) not in valid_ids:
                print("Data tidak tersedia. Silakan pilih monster yang ada pada list!")

            else:
                banyak = 1
                if item_type == 'potion':
                    banyak = int(input("Masukkan jumlah : "))

            if item_type == 'monster':
                valid_ids = [row[0] for row in monster_shop]
                for i in range(len(monster_shop)):
                    if monster_shop[i][0] == str(item_id):
                        for monster in monster_inventory:
                            if monster[0] == str(user_id) and monster[1] == monster_shop[i][0]:
                                monster_name = monster_shop[i][1]
                                print(f"Kamu sudah memiliki {monster_name}. Pembelian dibatalkan.")
                                break

                        else:
                            if oc_user >= int(monster_shop[i][-1]) * banyak and int(monster_shop[i][-2]) >= banyak:
                                oc_user -= int(monster_shop[i][-1]) * banyak
                                monster_shop[i][-2] = str(int(monster_shop[i][-2]) - banyak)
                                data.monster_inven.append([user_id, item_id, 1])
                                print("Pembelian berhasil! Monster sudah masuk ke inventory mu.")
                                print(f"O.W.C.A mu sekarang adalah {oc_user}")
                                data.user[user_id][4] = oc_user
                            else:
                                print("Yah, sayang sekali OC mu tidak cukup atau barang telah habis terjual :(")
                        break

            elif item_type == 'potion':
                valid_ids = [row[0] for row in tmp_potion]
                for i in range(len(tmp_potion)):
                    if tmp_potion[i][0] == str(item_id):
                        if oc_user >= int(tmp_potion[i][-1]) * banyak and int(tmp_potion[i][-2]) >= banyak:
                            oc_user -= int(tmp_potion[i][-1]) * banyak
                            tmp_potion[i][-2] = str(int(tmp_potion[i][-2]) - banyak)
                            data.item.append([user_id, tmp_potion[item_id][0], banyak])
                            print("Pembelian berhasil! Item sudah masuk ke inventory mu.")
                            print(f"O.W.C.A mu sekarang adalah {oc_user}")
                            data.user[user_id][4] = oc_user
                        else:
                            print("Yah, sayang sekali OC mu tidak cukup atau barang telah habis terjual :(")
                        break
            
            for i in range(1, len(tmp_potion)):
                item_shop[i][0] = tmp_potion[i][1]
                item_shop[i][1] = tmp_potion[i][2]
                item_shop[i][2] = tmp_potion[i][3]

            data.monster_shop = monster_shop
            data.stuff = item_shop

        elif choice ==  "keluar":
            print("Sampai jumpa! Silakan berbelanja lagi ya!! (* w *)")
            break
        else:
            print("Input tidak valid!")

def update_user_oc(id, oc_user, user):
    for i in range(1, len(user)):
        if user[i][0] == str(id):
            user[i][4] = oc_user
            break

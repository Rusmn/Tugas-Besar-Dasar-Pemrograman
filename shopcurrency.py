import data # type: ignore
import inputs, ui# type: ignore

data.load_data('data')

user =[]
monster = []
monster_inventory = []
monster_shop = []
item = []
item_inventory = []
item_shop = []
potion = [[0,"None"] , [1,"strength"] , [2,"resilience"] , [3,"healing"]]

def update_data():
    global user, monster, monster_inventory, monster_shop, item, item_inventory, item_shop

    user = data.user
    monster = data.monster
    monster_inventory = data.monster_inven
    monster_shop = data.monster_shop
    item = data.item
    item_inventory = data.item
    item_shop = data.stuff
    
def simpan_data():
    global user, monster, monster_inventory, monster_shop, item, item_inventory, item_shop

    data.user = user
    data.monster = monster
    data.monster_inven = monster_inventory
    data.monster_shop = monster_shop
    data.item = item
    data.item_inventory = item
    data.stuff = item_shop

monster_update = []
item_update = []

def tampilkan_monster():
    update_data()
    ui.border("MONSTER")
    print()
    headers = ["ID", "Type", "ATK Power", "DEF Power" ,"HP" ,"Stok", "Harga"]
    ui.table(headers, monster_shop)
    print()

def tampilkan_item():
    update_data()
    ui.border("POTION")
    print()
    print("ID \t Type    \t Stok \t Harga")
    print("=======================================")
    for i in range (1, len(item_shop)):
        print(f"{i} \t {item_shop[i][0]} \t {item_shop[i][1]} \t {item_shop[i][2]}")
    print()

def shopcurrency(user_id):
    global user, monster_inventory, item_inventory

    oc_user = int(data.user[user_id][4])
    print("Selamat datang di SHOP!!! Pastikan O.W.C.A mu cukup ya !!! (^ w ^)")

    while True:
        choice = input("Pilih aksi (lihat/beli/keluar) : ")

        if choice == "lihat":

            item_type = input("Mau lihat apa??? (monster/potion): ")
            if item_type == 'monster':
                print("Monster Shop:")
                tampilkan_monster()

            elif item_type == 'potion':
                print("Potion Shop:")
                tampilkan_item()

        elif choice == "beli":
            print(f"Jumlah O.W.C.A mu sekarang adalah {oc_user} OC.")

            valid_item_types = ['monster', 'potion']
            item_type = input("Mau beli apa??? (monster/potion): ")

            while item_type not in valid_item_types:
                print("Input tidak valid. Silakan pilih ulang.")
                item_type = input("Mau beli apa??? (monster/potion): ")

            if item_type == 'monster':
                tampilkan_monster()
            elif item_type == 'potion':
                tampilkan_item()

            item_id = int(input("Masukkan ID yang mau kamu beli : "))

            if item_type == 'monster':
                for i in range(1, len(data.monster_shop)):
                    if int(data.monster_shop[i][0]) == item_id:
                        for monster in data.monster_inven:
                            if int(monster[0]) == user_id and int(monster[1]) == item_id:
                                monster_name = data.monster[int(monster[1])][1]
                                print(f"Kamu sudah memiliki {monster_name}. Pembelian dibatalkan.")
                                break
                        else:
                            if oc_user >= int(data.monster_shop[i][-1]):
                                oc_user -= int(data.monster_shop[i][-1])
                                data.monster_shop[i][-2] = str(int(data.monster_shop[i][-2]) - 1)
                                data.monster_inven.append([user_id, item_id, 1])
                                print("Pembelian berhasil! Monster sudah masuk ke inventory mu.")
                                print(f"O.W.C.A mu sekarang adalah {oc_user}")
                            else:
                                print("Yah, sayang sekali OC mu tidak cukup :(")
                        break

            elif item_type == 'potion':
                for i in range(1, len(data.stuff)):
                    if int(data.stuff[i][0]) == item_id:
                        if oc_user >= int(data.item_shop[i][-1]):
                            oc_user -= int(data.item_shop[i][-1])
                            data.stuff[i][-2] = str(int(data.item_shop[i][-2]) - 1)
                            data.item.append([user_id, item_id, 1])
                            print("Pembelian berhasil! Item sudah masuk ke inventory mu.")
                            print(f"O.W.C.A mu sekarang adalah {oc_user}")
                        else:
                            print("Yah, sayang sekali OC mu tidak cukup :(")
                        break

            data.simpan_data()

        elif choice == "keluar":
            print("Sampai jumpa! Silakan berbelanja lagi ya!! (* w *)")
            break

        else:
            print("Input tidak valid!")

def update_monster_inven(arr, idx, is_monster=True):
    global monster_inventory, item_inventory, monster_update, item_update
    if is_monster:
        inventory = monster_inventory
        update_list = monster_update
    else:
        inventory = item_inventory
        update_list = item_update

    for i in range(len(inventory)):
        if (inventory[i][0] == update_list[idx][3] and inventory[i][1] == update_list[idx][4]):
            inventory[i][2] = update_list[idx][2]

    simpan_data()


shopcurrency(2)
import data # type: ignore
import inputs, ui # type: ignore

data.load_data('data')

'''==================== F11 - Laboratory ===================='''

monster_inventory = []
user = []
monster = []

def update_data():
    global monster_inventory, user, monster

    monster = data.monster
    monster_inventory = data.monster_inven
    user = data.user

def simpan_data():
    global monster_inventory, user, monster

    data.monster_inven = monster_inventory
    data.user = user
    data.monster = monster

monster_update = []

def inventory_data(user_id):
    global monster_inventory,user,monster,monster_update

    idx = 1

    for i in range (1,len(monster_inventory)):
        if(int(monster_inventory[i][0]) == user_id):
            print(f"{idx}.{monster[int(monster_inventory[i][1])][1]}, Level : {monster_inventory[i][2]}")
            monster_update.append([idx, monster[int(monster_inventory[i][1])][1], monster_inventory[i][2], monster_inventory[i][0], monster_inventory[i][1]])
            idx+=1

def laboratory(user_id):
    update_data()
    global user, monster_update
    oc_user = int(user[user_id][4])

    harga_upgrade = {
        1: 300,
        2: 500,
        3: 800,
        4: 1000,
    }

    ui.border("Selamat datang di laboratory!")

    ui.border("List monster milikmu:")
    inventory_data(user_id)

    ui.border("Harga Upgrade:")
    for level in harga_upgrade:
        print(f"Level ({level} -> {level+1}) : {harga_upgrade[level]}")

    print()
    ui.border(f"Jumlah koin yang dimiliki: {oc_user} OC")
    print()

    monster_choice = input("Pilih monster yang ingin diupgrade atau ketik keluar untuk batal: ")
    
    if(monster_choice.lower() == "keluar"):
        return

    while(not inputs.is_in_range(monster_choice, 1, len(monster_update))):
        monster_choice = input("Pilih monster yang ingin diupgrade atau ketik keluar untuk batal: ")
        if(monster_choice.lower() == "keluar"):
            return
    print()
    monster_choice = int(monster_choice)

    level_sekarang = int(monster_update[monster_choice-1][2])
    level_selanjutnya = level_sekarang + 1

    if level_selanjutnya >= 5:
            ui.border("Oh tidak! Monster ini sudah mencapai level maksimum! Silakan pilih monster lain yang ingin diupgrade.")
    else:
        harga = harga_upgrade[level_sekarang] if level_selanjutnya in harga_upgrade else 0
            
        if oc_user < harga:
            print(f"Koin tidak cukup! Kamu butuh {harga} OC untuk upgrade.")
        else:
            konfirmasi = input(f"Upgrade Monster {monster_update[monster_choice-1][1]} dari Lv {level_sekarang} ke Lv {level_selanjutnya}? (y/n): ")
            if konfirmasi.lower() == 'y': 
                oc_user -= harga
                user[user_id][4] = oc_user
                monster_update[monster_choice-1][2] = level_selanjutnya
                update_monster_inven(monster_update, monster_choice-1)
                ui.border(f'''
Monster {monster_update[monster_choice-1][1]} telah naik ke Lv {level_selanjutnya}.
Sisa koin: {oc_user} OC
''')

            else:
                print("Upgrade dibatalkan.")

    simpan_data()

def update_monster_inven(arr,idx):
    global monster_inventory
    for i in range(len(monster_inventory)):
        if(monster_inventory[i][0] == monster_update[idx][3] and monster_inventory[i][1] == monster_update[idx][4]):
            monster_inventory[i][2] = monster_update[idx][2]

    simpan_data()

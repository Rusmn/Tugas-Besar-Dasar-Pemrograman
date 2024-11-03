import inputs, ui # type: ignore
import data # type: ignore

''' ==================== F07 - Inventory ===================='''

monster = []
inven = []
stuff = []


def update_data():
    global inven, monster, stuff

    monster = data.monster
    inven = data.monster_inven
    stuff = data.item

def simpan_data():

    global inven, monster, stuff

    data.monster = monster
    data.monster_inven = inven
    data.item = stuff

    
monster_user = []
potion = [0 for i in range (3)]

batas = 0

def simpan_monster(user_id):
    update_data()
    global monster_user, batas
    for i in range (1, len(inven)):  
        if(user_id == int(inven[i][0])):
            id = monster[int(inven[i][1])][0] #id
            nama = monster[int(inven[i][1])][1] #nama
            atk = monster[int(inven[i][1])][2] #atk
            deff = monster[int(inven[i][1])][3] #def
            hp = monster[int(inven[i][1])][4] #hp
            lvl = inven[i][2] #level
            monster_user.append([id, nama, atk, deff, hp, lvl])
            batas+=1
    simpan_data()
 
def simpan_potion(user_id):
    update_data()
    global potion
    for i in range (1, len(stuff)):
        if(int(user_id) == int(stuff[i][0])):
            if (stuff[i][1] == "strength"):
                potion[0] = int(stuff[i][2])
            elif(stuff[i][1] == "healing"):
                potion[2] = int(stuff[i][2])
            elif(stuff[i][1] == "resilience"):
                potion[1] = int(stuff[i][2])
    simpan_data()

def inventory(user_id):
    update_data()
    global monster_user, potion
    simpan_monster(user_id)
    simpan_potion(user_id)

    ui.border(f"INVENTORY LIST (User ID : {user_id})")
    print(f"Jumlah O.W.C.A. Coin-mu sekarang {inputs.user[int(user_id)][4]}")
    
    idx1 = 1 #penanda monster


    for i in range (len(monster_user)):

        print(f'''{idx1}. monster [Name: {monster_user[i][1]}, Lvl : {monster_user[i][5]}, HP : {monster_user[i][4]}]  ''')
        idx1+=1

    idx2 = 0

    if(potion[0] != 0):
        print(f"{idx1+idx2}. potion [Type : ATK, Qty : {potion[0]}]  ") 
        idx2 += 1
    if(potion[1] != 0):
        print(f"{idx1+idx2}. potion [Type : DEF, Qty : {potion[1]}]  ")
        idx2+=1
    if(potion[2] != 0):
        print(f"{idx1+idx2}. potion [Type : Heal, Qty : {potion[2]}]  ")
        idx2+=1

    print()
    pilihan = input("Ketikkan id untuk menampilkan detail item atau ketik keluar: ")
    print()

    while(pilihan.upper() != "KELUAR"):
        if(inputs.is_number(pilihan)):
            if(1 <= int(pilihan) and int(pilihan) < (idx1+idx2)):
                if(1 <= int(pilihan) and int(pilihan) < idx1):
                    tampilkan(monster_user, (int(pilihan)-1))
                    print()
                else:
                    tampilkan(potion, (int(pilihan)-idx1))
                    print()
            else:
                print("Pilihan tidak valid")
                print()
        else:
            if(pilihan.upper() !="KELUAR"):
                print("Pilihan tidak valid")
                print()
        
        pilihan = input("Ketikkan id untuk menampilkan detail item atau ketik keluar: ")

    simpan_data()

def tampilkan(arr, id):
    if(arr == monster_user):
        ui.border(f'''
Monster
Nama      : {monster_user[id][1]}
ATK Power : {monster_user[id][2]}
DEF Power : {monster_user[id][3]}
HP        : {monster_user[id][4]}
Level     : {monster_user[id][5]}
''')
    elif(arr == potion):
        if(potion[id] == 0):
            tampilkan(potion, id+1)
        else:
            if(id == 0):
                ui.border(f'''
Potion 
Type      : ATK
Quantitiy : {potion[0]}
            ''')
            elif(id == 1):
                ui.border(f'''
potion 
Type      : DEF
Quantitiy : {potion[1]}
            ''')
            elif(id == 2):
                ui.border(f'''
potion 
Type      : Heal
Quantitiy : {potion[2]}
            ''')



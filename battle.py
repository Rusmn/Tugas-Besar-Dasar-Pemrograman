#battle
import time
import data # type: ignore
import inputs  # type: ignore
import ui # type: ignore

'''
TO-DO :
1. Perbaiki UI
2. INGAT LEVEL BISA LEBIH DARI 1 (bervariasi antara 1-5), handle masalah ini    
'''

''' ===== F00 - Random Number ====='''
def lcg():
    a = 41 # Multiplier
    c = 13  # Increment
    m = 2**32  # Modulus (2^32 untuk 32-bit)
    x = int(time.time())
    x = (a * x + c) % m
    return x

def random(): 
    a = lcg() // 100
    c = lcg() 
    m = 2**32
    x = int(time.time())
    x = (a * x + c) % m
    return x

''' ==================== F08 - Battle ===================='''

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

id_musuh = 0

musuh = [0 for i in range (6)]

def panggil_musuh(level):
    global id_musuh,musuh
    update_data()
    id_musuh = random() % (len(monster)) #id musuh yang dipanggil sebagai lawan

    while (id_musuh == 0): #make sure tidak mengakses array indeks nol
        id_musuh = random() % (len(monster))

    musuh[0] = int(monster[id_musuh][0])
    musuh[1] = monster[id_musuh][1]
    musuh[2] = int(int(monster[id_musuh][2]) + (level-1)*0.1*int(monster[id_musuh][2]))
    musuh[3] = int(int(monster[id_musuh][3]) + (level-1)*0.1*int(monster[id_musuh][3]))
    musuh[4] = int(int(monster[id_musuh][4]) + (level-1)*0.1*int(monster[id_musuh][4]))
    musuh[5] = int(level)

    ui.border(f'''
{ui.monster1}
RAWWWWRRR, Monster {musuh[1]} telah munculll!!!!)
==================================================
Nama      : {musuh[1]}                         
ATK Power : {musuh[2]}                         
DEF Power : {musuh[3]}                         
HP        : {musuh[4]}                         
Level     : {musuh[5]}                         
==================================================
\n''')
    
def find_user_id():
    for i in range (1, len(inputs.user)):
        if(inputs.user[i][1] == inputs.nama):
            return i

batas = 1 

monster_user = [" " for i in range (6)]

def monster_list(cek):
    global user_id, batas, monster_user, musuh
    update_data()

    if(cek == 0):
        ui.border("MONSTER LIST")
        print()
        for i in range (1, len(inven)):
            if(user_id == int(inven[i][0])):
                print(f"{batas}. {monster[int(inven[i][1])][1]}")
                batas+=1
        print("\n")
    
    else:
        batas = 1
        for i in range (1, len(inven)):
            if(user_id == int(inven[i][0])):
                if(batas == cek):
                    monster_user[0] = int(monster[int(inven[i][1])][0])
                    monster_user[1] = monster[int(inven[i][1])][1]
                    monster_user[2] = int(int(monster[int(inven[i][1])][2]) + (int(inven[i][2]) - 1)*0.1*int(monster[int(inven[i][1])][2]))
                    monster_user[3] = int(int(monster[int(inven[i][1])][3]) + (int(inven[i][2]) - 1)*0.1*int(monster[int(inven[i][1])][3]))
                    monster_user[4] = int(int(monster[int(inven[i][1])][4]) + (int(inven[i][2]) - 1)*0.1*int(monster[int(inven[i][1])][4]))
                    monster_user[5] = int(inven[i][2])
                    return (monster[int(inven[i][1])][1])
                batas+=1
    return

potion = [0 for i in range (3)] #array of quantity
flag_potion = [True for i in range(3)]

def isi_potion():
    update_data()
    global potion
    for i in range (1, len(stuff)):
        if(user_id == int(stuff[i][0])):
            if (stuff[i][1] == "strength"):
                potion[0] = int(stuff[i][2])
            elif(stuff[i][1] == "healing"):
                potion[2] = int(stuff[i][2])
            elif(stuff[i][1] == "resilience"):
                potion[1] = int(stuff[i][2])

def tampilkan_potion():
    global flag_potion, potion

    ui.border("POTION LIST")
    print(f"1. Strength Potion (Qty : {potion[0]}) - Increases ATK Power")
    print(f"2. Resilience Potion (Qty : {potion[1]}) - Increases DEF Power")
    print(f"3. Healing Potion (Qty : {potion[2]}) - Restores Health")
    print("4. Cancel\n")
            

def battle(level):
    global user_id,musuh, monster_user
    user_id = inputs.id
    owca = [i for i in range(5,31)]
    update_data()
    panggil_musuh(level) 
    isi_potion()

    monster_list(0)
    pilihan = input("Pilih monster untuk bertarung: ")
    while(not inputs.is_in_range(pilihan, 0, batas)):
        pilihan = input("Pilih monster untuk bertarung: ")
    pilihan = int(pilihan)
    tampilkan_monster(pilihan)

    turn = 1
    maksimum_hp = monster_user[4]

    while(musuh[4] > 0 and monster_user[4] > 0):
        
        ui.border(f"TURN {turn} ({monster_user[1]})")
        print()
        print("1. Attack")
        print("2. Use Potion")
        print("3. Quit\n")

        pilihan = input("Pilih perintah: ")
        while(not inputs.is_in_range(pilihan, 1, 3)):
            pilihan = input("Pilih perintah: ")
        
        pilihan = int(pilihan)

        if(pilihan == 1):
            serangan, persen = Attack(monster_user)
            ui.border(f'''
SCHWINKKK {monster_user[1]} menyerang {musuh[1]}!!!
ATT : {serangan}({persen}%), Reduced by : {int(serangan*(musuh[3])/100)}({musuh[3]}%), ATT Results : {int(serangan - (serangan*(musuh[3])/100))}
''')
            musuh[4] = int(musuh[4] - (serangan - (serangan*(float(musuh[3]))/100)))
            if(musuh[4] < 0):
                musuh[4] = 0
            tampilkan(ui.monster1, musuh, musuh[4])
        elif(pilihan == 2):
            pakai_potion(maksimum_hp)
        else:
            print("Anda Berhasil Kabur dari Battle!!")
            break
        
        if(musuh[4] > 0):
            ui.border(f"TURN {turn} ({musuh[1]})")
            serangan, persen = Attack(musuh)
            ui.border(f'''
SCHWINKKK {musuh[1]} menyerang {monster_user[1]}!!!
ATT : {serangan}({persen}%), Reduced by : {int(serangan*(monster_user[3])/100)}({monster_user[3]}%), ATT Results : {int(serangan - (serangan*(monster_user[3])/100))}
''')
            monster_user[4] = int(monster_user[4] - (serangan - (serangan*(float(monster_user[3]))/100)))
            if(monster_user[4] < 0):
                monster_user[4] = 0
            tampilkan(ui.monster2, monster_user, monster_user[4])

        ubah_potion()

        if(monster_user[4] <= 0):
            print(f"Yahhh, Anda dikalahkan monster {musuh[1]}. Jangan menyerah, coba lagi !!!")
            break

        elif(musuh[4] <= 0):
            print(f"Selamat, Anda berhasil mengalahkan monster {musuh[1]} !!!")
            tmp = int(inputs.user[user_id][4])
            tmp += owca[random()%25]

            print(f"Total OC yang diperoleh {owca[random()%25]}")

            data.user[user_id][4] = str(tmp)
            break

        turn+=1
    
    simpan_data()
        
def Attack(arr):
    attack = 0
    if(arr == monster_user):
        x = (47*random()) % 31
        while(x == 0):
            x = random() % 31
    else:
        x = random() % 31 #[1,2,3....30,0]
        while(x == 0):
            x = random() % 31

    operasi = random() % 2 #nilai serangan bisa bertambah atau berkurang

    if(operasi % 2 == 0):
        attack = float(arr[2]) - (float(arr[2])*x/100)
        x = -1*x
    else:
        attack = float(arr[2]) + (float(arr[2])*x/100)

    return attack, x

def tampilkan(monster, arr, hp):
    ui.border(f'''
{monster}
{ui.bar_darah(hp)}
============================
Nama      : {arr[1]}
ATK Power : {int(arr[2])}
DEF Power : {arr[3]}
HP        : {hp}
============================
''')

def pakai_potion(maksimum_hp):
    global potion, monster_user, monster_user, flag_potion
    tampilkan_potion()
    pilihan = input("Pilih Perintah: ")
    while(not inputs.is_in_range(pilihan, 1, 4)):
        pilihan = input("Pilih Perintah: ")

    pilihan = int(pilihan)

    while(pilihan != 4): 
        if(pilihan == 1):
            if(potion[0] != 0 and flag_potion[0]):
                monster_user[2] += (monster_user[2]*5/100)
                flag_potion[0] = False
                potion[0] -= 1
                ui.border(f'''
Setelah meminum ramuan ini, aura kekuatan terlihat mengelilingi {monster_user[1]} dan gerakannya menjadi lebih cepat dan mematikan.
ATK Power {monster_user[1]} menjadi {int(monster_user[2])}.
''')
            elif(not flag_potion[0]):
                ui.border(f"Kamu mencoba memberikan ramuan ini kepada {monster_user}, namun dia menolaknya seolah-olah dia memahami ramuan tersebut sudah tidak bermanfaat lagi.")
            elif(potion[0] == 0):
                ui.border(f"Wah, kamu sedang tidak memiliki ramuan ini, silahkan pilih ramuan lain!")
        
        elif(pilihan == 2):
            if(potion[1] != 0 and flag_potion[1]):
                monster_user[3] += (monster_user[3]*5/100)
                flag_potion[1] = False
                potion[1] -= 1
                ui.border(f'''
Setelah meminum ramuan ini, muncul sebuah energi pelindung di sekitar {monster_user[1]} yang membuatnya terlihat semakin tangguh dan sulit dilukai.
DEF Power {monster_user[1]} menjadi {int(monster_user[3])}.
''')
            elif(not flag_potion[1]):
                ui.border(f"Kamu mencoba memberikan ramuan ini kepada {monster_user}, namun dia menolaknya seolah-olah dia memahami ramuan tersebut sudah tidak bermanfaat lagi.")
            elif(potion[1] == 0):
                ui.border(f"Wah, kamu sedang tidak memiliki ramuan ini, silahkan pilih ramuan lain!")
        
        elif(pilihan == 3):
            #pastikan hp tidak melebihi maksimal hp
            if(potion[2] != 0 and flag_potion[2]):
                if(monster_user[4]+(25/100*monster_user[4]) <= maksimum_hp):
                    monster_user[4] += (maksimum_hp*25/100)
                    flag_potion[2] = False
                    potion[2] -= 1
                    ui.border(f'''
Setelah meminum ramuan ini, muncul sebuah energi pelindung di sekitar {monster_user[1]} yang membuatnya terlihat semakin tangguh dan sulit dilukai.
HP {monster_user[1]} meningkat menjadi {int(monster_user[4])}.
''')
                else:
                    ui.border(f"Penambahan potion tidak bisa dilakukan")
            elif(not flag_potion[2]):
                ui.border(f"Kamu mencoba memberikan ramuan ini kepada {monster_user[1]}, namun dia menolaknya seolah-olah dia memahami ramuan tersebut sudah tidak bermanfaat lagi.")
            elif(potion[2] == 0):
                ui.border(f"Wah, kamu sedang tidak memiliki ramuan ini, silahkan pilih ramuan lain!")  

        tampilkan_potion()
        pilihan = input("Pilih Perintah: ")
        while(not inputs.is_in_range(pilihan, 1, 4)):
            pilihan = input("Pilih Perintah: ")
        
        pilihan = int(pilihan)
       

def ubah_potion():
    global stuff, user_id
    for i in range (1, len(stuff)):
        if(int(user_id) == int(stuff[i][0])):
            if (stuff[i][1] == "strength"):
                stuff[i][2] = potion[0]
            elif(stuff[i][1] == "healing"):
                stuff[i][2] = potion[2]
            elif(stuff[i][1] == "resilience"):
                stuff[i][2] = potion[1]

def tampilkan_monster(pilihan):
    global monster_user

    ui.border(f'''
{ui.monster2}
RAWWWRRRR!!!!, Agent {inputs.nama} memanggil monster {monster_list(pilihan)}
==================================================
Nama      : {monster_user[1]}                         
ATK Power : {monster_user[2]}                         
DEF Power : {monster_user[3]}                         
HP        : {monster_user[4]}                         
Level     : {monster_user[5]}
==================================================
''')
    
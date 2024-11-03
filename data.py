import os
import utility, ui # type: ignore
import time

#PERHATIKAN !!! Data CSV harus disalin ke setiap file mereka.

data = []

def read_csv(file_path, delimiter=','):
    data = []
    with open(file_path, 'r') as file:
        for line in file:
            # Hilangkan karakter newline di akhir setiap baris
            line = utility.remove_space(line)
            # Pisahkan baris menjadi list berdasarkan delimiter
            row = utility.custom_split(line, delimiter)
            # Tambahkan baris ke dalam data
            data.append(row)
    return data

def input_csv(file_path, data):
    with open(file_path, 'a') as file:
        # Menggunakan join untuk menggabungkan data menjadi satu string dengan delimiter koma
        line = utility.gabung_string(data)
        line = utility.remove_space(line)
        file.write(line + '\n')

'''ubah file csv'''

def rewrite_csv(file_path):
    global data
    if('item_inventory.csv' in file_path):
        data = ["user_id","type" , "quantity"]
    elif('item_shop.csv' in file_path):
        data = ["type" , "stok" , "harga"]
    elif('monster.csv' in file_path):
        data = ["id" ,"type" , "atk_power" ,"def_power" , "hp"]
    elif('user.csv' in file_path):
        data = ["id","username","password","role","oc"]
    elif('monster_inventory' in file_path):
        data = ["user_id" ,"monster_id", "level"]
    elif('monster_shop.csv' in file_path):
        data = ["id" ,"type", "atk_power" ,"def_power","hp","stok","harga"]
    with open(file_path, 'w') as file:
        line = utility.gabung_string(data)
        line = utility.remove_space(line)
        file.write(line + '\n')

def data_to_csv(file_path, arr):
    rewrite_csv(file_path)
    for i in range(1, len(arr)):
        tmp = []
        for j in range(len(arr[i])):
            tmp.append(arr[i][j])

        input_csv(file_path, tmp)

'''==================== F14 - Load ===================='''
#membaca keseluruhan file csv

monster = []
item = []
user =[]
monster_inven = []
stuff = []
monster_shop = []

def load_data(folder_name):
    global monster, item, user, monster_inven, stuff, monster_shop  
    #untuk load data, perhatikan folder semua yang lain harus mengarah pada data base, kecuali data monster inventory, dan item inventory

    if folder_name != 'data':
        folder_name = os.path.join("data", folder_name)

    if (not os.path.exists(folder_name)):

        ui.border(ui.owca)

        ui.border(f"Folder {folder_name} tidak ada. Periksa kembali nama folder yang anda masukkan")

        exit()
    
    #yang di load hanya yang data item (pribadi), sisanya load data base

    path = os.path.join('data', "monster.csv")
    monster = read_csv(path)
    path = os.path.join(folder_name, "item_inventory.csv")
    item = read_csv(path)
    path = os.path.join('data', "user.csv")
    user = read_csv(path)
    path = os.path.join(folder_name, "monster_inventory.csv")
    monster_inven = read_csv(path)
    path = os.path.join('data', "item_shop.csv")
    stuff = read_csv(path)
    path = os.path.join('data', "monster_shop.csv")
    monster_shop = read_csv(path)

'''==================== F15 - Save ===================='''
#menyimpan file csv  

def save_file(folder_name):
    global monster, item, user, monster_inven, stuff, monster_shop 
    
    parent_dir = "data"
    path = os.path.join(parent_dir, folder_name)

    print('Saving...')

    for i in ('...'):
        print(i)
        time.sleep(1)
    print()

    if not os.path.exists(path):
        ui.border(f"Membuat folder {path}")
        os.makedirs(path)


    if(folder_name != 'data'):
        data_to_csv(os.path.join('data', 'monster.csv'), monster),
        data_to_csv(os.path.join('data', 'item_inventory.csv'), item),
        data_to_csv(os.path.join('data', 'user.csv'), user),
        data_to_csv(os.path.join('data', 'monster_inventory.csv'), monster_inven),
        data_to_csv(os.path.join('data', 'item_shop.csv'), stuff),
        data_to_csv(os.path.join('data', 'monster_shop.csv'), monster_shop)

    data_to_csv(os.path.join(path, 'monster.csv'), monster),
    data_to_csv(os.path.join(path, 'item_inventory.csv'), item),
    data_to_csv(os.path.join(path, 'user.csv'), user),
    data_to_csv(os.path.join(path, 'monster_inventory.csv'), monster_inven),
    data_to_csv(os.path.join(path, 'item_shop.csv'), stuff),
    data_to_csv(os.path.join(path, 'monster_shop.csv'), monster_shop)
    
    data_to_csv(os.path.join('data', 'monster.csv'), monster),
    data_to_csv(os.path.join('data', 'item_inventory.csv'), item),
    data_to_csv(os.path.join('data', 'user.csv'), user),
    data_to_csv(os.path.join('data', 'monster_inventory.csv'), monster_inven),
    data_to_csv(os.path.join('data', 'item_shop.csv'), stuff),
    data_to_csv(os.path.join('data', 'monster_shop.csv'), monster_shop)

    ui.border(f"Berhasil menyimpan data pada {path}")
    






    
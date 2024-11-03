import ui, inputs, help, battle, data, inventory, utility, management, shop, arena, shop_currency # type: ignore
from laboratory import laboratory # type: ignore
import argparse, time, os

#TO-DO : PASTIKAN SEMUA INPUT BERTIPE STRING, KEMUDIAN NANTI DISESUAIKAN DENGAN FUNGSI-FUNGSI YANG ADA, MANFAATKAN YANG TELAH TERSEDIA DI INPUTS
#UNTUK SEMUA PERUBAHAN HARUS DI SAVE DULU, TIDAK BOLEH LANGSUNG DISAVE
#Pembacaan array diawal saja pertama kali, agar ketika game berjalan tidak perlu bolak-balik, mekanisme save perlu ditinjau
'''
F01 50
F02 50
F03 50
F04 50 -> Pastikan apakah data sudah harus disimpan ataukah tidak?
F05 50 -> monster.csv benahi lagi, perhatikan batas data
F06 50 -> perbaiki item_inventory.csv
F07 50 
F08 50 -> simulasikan lebih banyak tes case 
F09 X
F10 X 
F11 50 -> banyak hal yang harus dipastikan lagi
F12 40 -> perhatikan input/output, pastikan "del arr[] boleh"
F13 50 -> perhatikan input/output
F14 25 -> perhatikan file yang di load
F15 25 -> perhatikan file apa saja yang disave
F16 25 -> benahi mekanisme save
'''

os.system('cls')
msg = r'''
Silahkan ketik 'HELP' pada command untuk menampilkan daftar perintah.
                Atau ketik perintah yang tersedia.
              '''

def main():
    parser = argparse.ArgumentParser(description= '===== O.W.C.A Game =====') 
    parser.add_argument('nama_folder', metavar = 'nama_folder', type = str, help = 'Nama folder berisi data eksternal.')
    args = parser.parse_args()

    print('Loading...')

    for i in ('...'):
        print(i)
        time.sleep(1)
    print()

    data.load_data(args.nama_folder)   

    ui.border(ui.selamat_datang)
    time.sleep(1.5)
    print()

    os.system('cls')

    ui.border(ui.owca)

    while(True):

        ui.border(msg)
        print()
        choice = input("Ketik Perintah: ")
        choice = utility.remove_space(choice)
        print()

        if(choice.upper() == "REGISTER"):
            if(inputs.cek_login):

                ui.border(ui.regis)
                inputs.regis()
            else:
                print("Register gagal!")
                print(f"Anda telah login dengan username {inputs.nama}, silahkan lakukan “LOGOUT” sebelum melakukan register.")
                print()

        elif(choice.upper() == "LOGIN"):
            if(inputs.cek_login):

                ui.border(ui.login)
                inputs.login()
            else:
                print("Login gagal!")
                print(f"Anda telah login dengan username {inputs.nama}, silahkan lakukan “LOGOUT” sebelum melakukan login kembali.")
                print()

        elif(choice.upper() == "HELP"):

            ui.border(ui.help)
            if(inputs.cek_login):
                help.help1()
            elif(data.user[inputs.id][3] == "agent"):
                help.help2()
            elif(data.user[inputs.id][3] == "admin"):
                help.help3()

        elif(choice.upper() == "INVENTORY"):
            if(data.user[inputs.id][3] == "admin"):
                print("Maaf bagian ini khusus untuk agent.")
                print()
            elif(not inputs.cek_login):

                ui.border(ui.inventory)
                inventory.inventory(inputs.id)
                print()
            else:
                print("Maaf anda belum login.")

        elif(choice.upper() == "LOGOUT"):
            inputs.logout()

        elif(choice.upper() == "BATTLE"):
            if(data.user[inputs.id][3] == "admin"):
                print("Maaf bagian ini khusus untuk agent.")
                print()
            elif(not inputs.cek_login):

                ui.border(ui.battle)
                level = battle.random() % 5
                while(level == 0):
                    level = battle.random() % 5
                battle.battle(level)
            else:
                print("Maaf Anda Belum Login.")
                print()
        elif(choice.upper() == "ARENA"):
            if(data.user[inputs.id][3] == "admin"):
                print("Maaf bagian ini khusus untuk agent.")
                print()
            elif(not inputs.cek_login):

                ui.border(ui.arena)
                arena.arena()
            else:
                print("Maaf Anda Belum Login.")
                print()
        elif(choice.upper() == "LABORATORY"):
            if(data.user[inputs.id][3] == "admin"):
                print("Maaf bagian ini khusus untuk agent.")
                print()
            elif(not inputs.cek_login):
   
                ui.border(ui.laboratory)
                laboratory(inputs.id)
                print()
            else:
                print("Maaf Anda Belum Login")
                print()

        elif(choice.upper() == "MONSTER"):
            if(data.user[inputs.id][3] == "agent"):
                print("Maaf anda bukan admin.")
                print()
            elif(not inputs.cek_login):

                management.monster_admin()
            else:
                print("Maaf Anda Belum Login.")
                print()
        
        elif(choice.upper() == "SHOP"):
            if(data.user[inputs.id][3] == "agent"):
                ui.border(ui.shop)
                shop_currency.shopcurrency(inputs.id)
                print()
            elif(data.user[inputs.id][3] == "admin"):

                ui.border(ui.shop)
                ui.border("Selamat Datang di Shop Management, sebagai Admin anda bebas untuk mengedit data pada Shop")
                print()
                shop.shop_admin()
            else:
                print("Maaf Anda Belum Login.")
                print()

        # ===== F16 - Exit=====
        elif(choice.upper() == "EXIT"):
            if(not inputs.cek_login):
                mau_save = input("Apakah Anda mau melakukan penyimpanan file yang sudah diubah? (y/n) ")

                while(mau_save.lower() != 'y' and mau_save.lower() != 'n'):
                    mau_save = input("Apakah Anda mau melakukan penyimpanan file yang sudah diubah? (y/n) ")

                if(mau_save.lower() == 'y'):
                    folder = input("Masukkan nama folder: ")
                    data.save_file(folder)
                    break
                elif(mau_save.lower() == 'n'):
                    break
            else:
                break
        else:
            ui.border("Harap Masukkan sesuai perintah!!!  ")
    
    ui.border(ui.selesai)
    ui.border("TERIMA KASIH SUDAH BERMAIN, JANGAN LUPA BERKUNJUNG LAGI")
    
if (__name__ == '__main__') :
    main()

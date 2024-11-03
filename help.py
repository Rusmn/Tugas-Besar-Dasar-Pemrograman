import inputs, ui # type: ignore

'''==================== F04 - Menu & Help ===================='''

def help1(): #belum login
    ui.border('''
Kamu belum login sebagai role apapun. Silahkan login terlebih dahulu.

LOGIN    : Masuk ke dalam akun yang sudah terdaftar.
REGISTER : Membuat akun baru.
EXIT     : Keluar dari permainan, tanpa melakukan apapun.
          ''')
    
def help2():#sudah login Agent

    ui.border('''
Halo Agent {inputs.nama} Kamu memanggil command HELP. Kamu memilih jalan yang benar, semoga kamu tidak sesat kemudian. 
Berikut adalah hal-hal yang dapat kamu lakukan sekarang:

INVENTORY : Menampilkan data inventory.
BATTLE    : Memulai pertarungan dengan berbagai monster dengan level acak (1-5).
ARENA     : Melatih monster, dengan melawan monster lain hingga stage 5.
SHOP      : Membeli monster atau item.
LOGOUT    : Keluar dari akun yang sedang digunakan.
EXIT      : Menyelesaikan permainan.
        ''')
    
def help3():

    ui.border('''
Selamat datang, Admin. Berikut adalah hal-hal yang dapat kamu lakukan:

SHOP    : Melakukan Shop Management.
MONSTER : Melakukan Monster Management.
LOGOUT  : Keluar dari akun.
''')

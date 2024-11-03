import csv
import data # type: ignore
import utility # type: ignore
import save_iq# type: ignore

#[0][0] [][]
'''
monsters = {}

def tersedia_username(c):
    with open('user.csv', mode='r') as file:
        reader = csv.reader(file)
        print (reader)
        for row in reader:
            if row and row[1] == c:
                return True
    return False

data = data.read_csv('monster.csv')
for row in data:
    monsters[int(row[0])] = row[1]

print(monsters)


list = [10, 'tes', 11, 'tes2']

new_list = utility.gabung_string(list)

def bulat(x):
    return int(x)

x = float(input())

print(bulat(x))


tmp = [] 
n=0
arr = [[1,2,3],[1,2,5]]

print(len(arr[0]))

print(arr)
'''
folder_name = input()
data.load_data(folder_name)
folder_name = input()  
data.save_file(folder_name)

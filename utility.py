
def cek_space(s):
    return (s == ' ') or (s == '\n')

def custom_split(string, delimiter):
    result = []
    current_word = ''
    for char in string:
        if char == delimiter:
            result.append(current_word)
            current_word = ''  
        else:
            current_word += char
    result.append(current_word)
    return result

def remove_space(string):
    start_index = 0
    end_index = len(string) - 1
    while start_index <= end_index and cek_space(string[start_index]):
        start_index += 1
    while end_index >= start_index and cek_space(string[end_index]):
        end_index -= 1
    return string[start_index:end_index + 1]

def cek_space(s):
    return (s == ' ') or (s == '\n')

def gabung_string(arr):
    tmp_string = ' '
    for i in range (len(arr)):
        if(i != len(arr)-1):
            tmp_string += str(arr[i])
            tmp_string += ','
        else :
            tmp_string += str(arr[i]) 
    
    return tmp_string

def find_max_length(lengths):
    max_length = 0
    for length in lengths:
        if length > max_length:
            max_length = length
    
    return max_length

def del_idx(arr, idx):
    tmp = []
    for i in range (len(arr)):
        if (i != idx):
            tmp.append(arr[i])
    return tmp






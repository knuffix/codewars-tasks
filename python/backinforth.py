# https://www.codewars.com/kata/60cc93db4ab0ae0026761232

def arrange(s_arr:list) -> list:
    
    if len(s_arr) <= 1:
        return s_arr
    tmp: list = []
    tmp.append(s_arr[0])
    tmp.append(s_arr[len(s_arr)-1])
    for ind in range(1, len(s_arr)//2):
        if ind % 2 == 1:
            tmp.append(s_arr[len(s_arr) - 1 - ind])
            tmp.append(s_arr[ind])
        else:
            tmp.append(s_arr[ind])
            tmp.append(s_arr[len(s_arr) - 1 - ind])
    if len(s_arr) % 2 == 1: tmp.append(s_arr[len(s_arr)//2])
    return tmp
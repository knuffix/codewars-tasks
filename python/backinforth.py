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
# [9, 7, -2, 8, 5, -3, 6, 5, 1]         
# {}

# [7, -2, 8, 5, -3, 6, 5]
# {9,1}  0 n

# [5,6,-3,5,8,-2,7]
# {9,1}

# [6,-3,5,8,-2]
# {9,1,5,7}  0 n n-1 1

# [-2,8,5,-3,6]     
# {9,1,5,7}

# [8,5,-3]
# {9,1,5,7,-2,6}   0 n n-1 1 2 n-2
print(arrange([9, 7, -2, 8, 5, -3, 6, 5, 1]))
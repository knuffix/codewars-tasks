# https://www.codewars.com/kata/59f4a0acbee84576800000af 
# bad description
# not solved, bcs all_pos must be in all combinations
# example in description not excess


def pos_average(s:str)-> float:
    arr:list = s.split(', ')
    common: int = 0
    all_pos: int = 0
    counter = 0
    queue:list = []
    for el in arr:
        for el2 in arr:
            if el != el2 and not el2 in queue:
                counter += 1
                for i in range(0, len(el2)):
                    if el2[i] == el[i]:                    
                        common += 1
                    all_pos += 1
        queue.append(el)
    return (common/all_pos) * 100
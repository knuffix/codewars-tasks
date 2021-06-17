#https://www.codewars.com/kata/598c1bc6a04cd3b8dd000012

def restaurant(single_tables, double_tables, visitors):
    one_seated = single_tables
    duo_seated = double_tables
    occ_seated = 0
    sad_people = 0
    for visitor in visitors:
        print(f'Come {visitor}\n vacant one-seated {one_seated}\n vacant duo-seated {duo_seated}')
        if visitor == 1:
            if one_seated > 0:
                one_seated -= 1
            elif duo_seated > 0:
                duo_seated -=1
                occ_seated +=1
            elif occ_seated > 0:
                occ_seated -= 1
            else:
                sad_people +=visitor
        else:
            if duo_seated > 0:
                duo_seated -=1
            else:
                sad_people +=visitor
    return sad_people


print(restaurant(0, 2, [1, 1, 2]))


# https://www.codewars.com/kata/5659c6d896bc135c4c00021e/

# Checking from right to left for first
# digit which has lesser digit from right side
# example:
# input is 9897165936723601601123356666778999
# 9897165936723601|6|011233(5)6666778999
# 1. digit 6 has less digit from right side (5)
# 2. 'swap' that digit and its less target
# 3. saving all left part WITH new swapped digit
# 4. we have digits in right side with 6 and we need to
#    create max possible number from this digits
# 5. just sorting this list and reverse
# 6. add this to our saved left part
# 7. PROFIT?!?
# Additional checks: 
# - result is lower then input 
# - result not starts with 0 (zero)
# 9897165936723601599987766666332110
def next_smaller(n: int) -> int:
    digits: list = ','.join(str(n)).split(',')
    for ind in range(len(digits) - 2, -1, -1):
        for jind in range(len(digits)-1, ind, -1):
            if int(digits[ind]) > int(digits[jind]):
                res = ''.join(digits[:ind]) + digits[jind]
                if res.startswith('0'):
                    continue
                new_digits = digits[ind:]
                new_digits.pop(new_digits.index(digits[jind]))
                res += ''.join(map(lambda x: str(x),
                               sorted(map(lambda x: int(x), new_digits),
                                      reverse=True)))
                if int(res) < n:
                    return int(res)
    return -1

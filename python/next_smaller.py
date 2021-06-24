# https://www.codewars.com/kata/5659c6d896bc135c4c00021e/


def next_smaller(n: int) -> int:
    digits: list = ','.join(str(n)).split(',')
    res = ''
    # for R->L
    for ind in range(len(digits) - 2, -1, -1):
        # For L->R
        for jind in range(len(digits)-1, ind, -1):
            if int(digits[ind]) > int(digits[jind]):
                res = ''.join(digits[:ind]) + digits[jind]
                if res.startswith('0'):
                    continue
                new_digits = digits[ind:]
                new_digits.pop(new_digits.index(digits[jind]))
                res += ''.join(map(lambda x: str(x),sorted(map(lambda x: int(x), new_digits), reverse=True)))
                if int(res) < n:
                    return int(res)
    return -1


tmp = next_smaller(
    9897165936723601601123356666778999)
assert tmp == 9897165936723601599987766666332110, f'\nShould be: 9897165936723601599987766666332110\n is given: {tmp} '

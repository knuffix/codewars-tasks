# https://www.codewars.com/kata/55983863da40caa2c900004e/

def next_bigger(n: int) -> int:
    str_num = str(n)
    if len(str_num) == 1:
        return -1
    digits = []
    for digit in str_num:
        digits.append(digit)
    if len(set(digits)) == 1:
        return -1
    min_number = int(''.join(sorted(digits)))
    max_number = int(''.join(sorted(digits, reverse=True)))
    if n == max_number:
        return -1
    perms = permutations(str_num)
    perms = set([int(i) for i in perms])
    perms = sorted(perms)
    return perms[perms.index(n) + 1]


def permutations(s):
    if len(s) <= 1:
        return [s]
    else:
        perms = []
        for e in permutations(s[:-1]):
            for i in range(len(e)+1):
                if e[:i] + s[-1] + e[i:] not in perms:
                    perms.append(e[:i] + s[-1] + e[i:])
        return perms


print(next_bigger(2000000000000017))

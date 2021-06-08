# https://www.codewars.com/kata/54eb33e5bc1a25440d000891
# My little sister came back home from school with the following task: given a squared sheet of paper she has to cut it in pieces which, when assembled, give squares the sides of which form an increasing sequence of numbers. At the beginning it was lot of fun but little by little we were tired of seeing the pile of torn paper. So we decided to write a program that could help us and protects trees.
# Task

# Given a positive integral number n, return a strictly increasing sequence (list/array/string depending on the language) of numbers, so that the sum of the squares is equal to n².

# If there are multiple solutions (and there will be), return as far as possible the result with the largest possible values:
# Examples

# decompose(11) must return [1,2,4,10]. Note that there are actually two ways to decompose 11², 11² = 121 = 1 + 4 + 16 + 100 = 1² + 2² + 4² + 10² but don't return [2,6,9], since 9 is smaller than 10.

# For decompose(50) don't return [1, 1, 4, 9, 49] but [1, 3, 5, 8, 49] since [1, 1, 4, 9, 49] doesn't form a strictly increasing sequence.
# Note

# Neither [n] nor [1,1,1,…,1] are valid solutions. If no valid solution exists, return nil, null, Nothing, None (depending on the language) or "[]" (C) ,{} (C++), [] (Swift, Go).

# The function "decompose" will take a positive integer n and return the decomposition of N = n² as:

#     [x1 ... xk] or
#     "x1 ... xk" or
#     Just [x1 ... xk] or
#     Some [x1 ... xk] or
#     {x1 ... xk} or
#     "[x1,x2, ... ,xk]"

# depending on the language (see "Sample tests")
import math


def recursive_find_sum(squares: list, sum: int) -> list:
    res = []
    tmp = []
    squares_copy = squares
    if sum < 0:
        return None
    for value in squares:
        #print(f'cur value {value}')
        tmp = []
        if sum - value == 0:
            tmp.append(int(math.sqrt(value)))
            tmp.append(int(
                math.sqrt(squares[squares.index(sum)])))
            return tmp
        elif (sum - value) in squares:
            tmp.append(int(math.sqrt(value)))
            tmp.append(int(
                math.sqrt(squares[squares.index(sum-value)])))
            return tmp
        else:
            tmp.append(int(math.sqrt(value)))
            x = recursive_find_sum(squares_copy, sum - value)
            if x:
                if type(x) is list:
                    for j in x:
                        tmp.append(j)
                else:
                    tmp.append(x)
        # print(tmp)
        res.append(tmp)
    return tmp


def decompose(n):
    import random
    square = n*n
    squares = {}
    for i in range(n-1, 0, -1):
        squares[i] = i*i
    results = recursive_find_sum(list(squares.values()), square)
    if not results:
        return None
    for i in [results.count(x) for x in results]:
        if i > 2:
            return None
    return sorted(results)


assert decompose(3) == [
    1, 2, 2], f"Should be [1,2,2], but given: {decompose(3)}"
print('decomposing 3 Success!')
assert decompose(5) == [3, 4], f"Should be [3,4], but given: {decompose(5)}"
print('decomposing 5 Success!')
assert decompose(6) == [
    1, 1, 3, 5], f"Should be [1,1,3,5], but given: {decompose(6)}"
print('decomposing 6 Success!')
assert decompose(8) == None, f'Should be None, but given: {decompose(8)}'
print('decomposing 8 Success!')
assert decompose(11) == [
    1, 2, 4, 10], f'Should be [1,2,4,10], but given {decompose(11)}'

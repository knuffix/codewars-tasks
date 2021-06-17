# https://www.codewars.com/kata/5672682212c8ecf83e000050/
from timeit import default_timer as timer


def dbl_linear(n, arr: set = None):
    if arr is None:
        arr = set([1])
    arr: set = arr
    tmp: set = arr.copy()
    for el in tmp:
        arr.add(2*el + 1)
        arr.add(3*el + 1)
        if len(arr) > 5*n:
            return sorted(list(arr))[n]
    return dbl_linear(n, arr)
def testing():
    start_time = timer()
    print(dbl_linear(6000))
    print(dbl_linear(6000))
    elapsed = timer() - start_time
    print('{:.5f} secs'.format(elapsed))

testing()
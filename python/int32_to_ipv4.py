# https://www.codewars.com/kata/52e88b39ffb6ac53a400022e

def int32_to_ip(int32: int):
    return '.'.join(['{0:d}'.format(int('{0:032b}'.format(int32)[i:i+8], base=2)) for i in range(0, 32, 8)])


print(int32_to_ip(32))

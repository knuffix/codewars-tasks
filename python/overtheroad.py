# https://www.codewars.com/kata/5f0ed36164f2bc00283aed07


def over_the_road(address: int, n: int) -> int:
    max_address: int = 2*n
    if address % 2 == 0:
        # if target on left side
        return max_address - address + 1
    else:
        # if target on right side
        return max_address - address + 1


assert over_the_road(
    1, 3) == 6, f'Should be 6 but {over_the_road(1,3)} is given'
assert over_the_road(
    3, 3) == 4, f'Should be 6 but {over_the_road(3,3)} is given'
assert over_the_road(
    3, 5) == 8, f'Should be 6 but {over_the_road(3,5)} is given'
assert over_the_road(
    23633656673, 310027696726) == 596421736780, f'Should be 6 but {over_the_road(23633656673,310027696726)} is given'

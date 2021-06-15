# https://www.codewars.com/kata/51fda2d95d6efda45e00004e/

class User():
    def __init__(self):
        self.rank = -8
        self.progress = 0
        self.__available_ranks = [-8, -7, -6, -5, -
                                  4, -3, -2, -1, 1, 2, 3, 4, 5, 6, 7, 8]

    def inc_progress(self, katas_rank: int):
        if not katas_rank in self.__available_ranks:
            raise Exception(f'There is no rank of {katas_rank}')
        if katas_rank == self.rank:
            self.progress += 3
        if katas_rank == self.rank - 1 or (katas_rank == -1 and self.rank == 1):
            self.progress += 1
        if katas_rank <= self.rank - 2 or (katas_rank == -1 and self.rank == 2) or (katas_rank == -2 and self.rank == 1):
            pass
        if katas_rank >= self.rank + 1:
            diff = 0
            if katas_rank > 0 and self.rank < 0:
                diff = katas_rank - self.rank - 1
            else:
                diff = abs(katas_rank - self.rank)
            self.progress += 10 * diff * diff
        self.__calc_rank()

    def __calc_rank(self):
        diff = abs(self.progress // 100)
        if self.rank >= 8:
            self.progress = 0
            return
        if diff > 0:
            if self.rank + diff >= 0 and self.rank < 0:
                if self.rank + diff + 1 >= 8:
                    self.rank = 8
                    self.progress = 0
                    return
                else:
                    self.rank += diff + 1
            else:
                if self.rank + diff >= 8:
                    self.rank = 8
                    self.progress = 0
                    return
                else:
                    self.rank += diff
            self.progress -= 100 * diff


user = User()
assert user.rank == -8
assert user.progress == 0
user.inc_progress(9)
assert user.progress == 0
print(user.progress)
print(user.rank)

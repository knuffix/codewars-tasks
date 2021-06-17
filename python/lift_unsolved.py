# https://www.codewars.com/kata/58905bfa1decb981da00009e/
from pprint import pprint
class Dinglemouse(object):

    def __init__(self, queues, capacity):
        self.capacity = capacity
        self.queues: list = [[x for x in i] for i in queues]
        self.floors_count = len(self.queues)
        self.current_floor = 0
        self.path = [0]

    def theLift(self):
        # creating max count entering passengers path on UP and DOWN direction
        # 
        return 0

tests = [[((),   (),    (5, 5, 5), (),   (),    (),    ()),     [0, 2, 5, 0]],
         [((),   (),    (1, 1),   (),   (),    (),    ()),     [0, 2, 1, 0]],
         [((),   (3,),  (4,),    (),   (5,),  (),    ()),     [0, 1, 2, 3, 4, 5, 0]],
         [((),   (0,),  (),      (),   (2,),  (3,),  ()),     [0, 5, 4, 3, 2, 1, 0]]]

for queues, answer in tests:
    lift = Dinglemouse(queues, 5)
    tmp = lift.theLift()
    assert tmp == answer, f'Should be {answer}, but {tmp} given'

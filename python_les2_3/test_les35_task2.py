import sys
import unittest
from les35_task2 import func


class TestsForLes32Task1(unittest.TestCase):
    class FakeStream:
        def __init__(self, file_name):
            self.msg = []
            self.file = file_name 
            self.gen = self.s_gen()

    def test_1(self):
        inp = '[{"name": "B", "parents": ["A", "C"]}, {"name": "C", "parents": ["A"]}, {"name": "A", "parents": []}, {"name": "D", "parents":["C", "F"]}, {"name": "E", "parents":["D"]}, {"name": "F", "parents":[]}]'
        ress = {'A':5,'B':1,'C':4,'D':2,'E':1,'F':3}
        with open('./file,json','w') as f:
            f.write(inp)
        with open('./file,json',) as f:
            self.assertEqual(ress, func(f))


if __name__ == '__main__':
    unittest.main()


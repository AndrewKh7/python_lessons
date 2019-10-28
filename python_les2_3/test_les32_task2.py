import sys
import unittest
FILE = 'les32_task2.py'


class TestsForLes32Task2(unittest.TestCase):
    class FakeStream:
        def __init__(self, s, t):
            self.msg = []
            self.t = t
            self.s = s
            self.gen = self.s_gen()

        def s_gen(self):
            yield self.s
            yield self.t

        def write(self,msg):
            self.msg.append(msg)

        def readline(self):
            return next(self.gen)

    def func_for_test(self, s, t):
        fake_frame = self.FakeStream(s, t)
        try:
            sys.stdin = sys.stdout = fake_frame
            with open(FILE) as f:
                exec(f.read())
        finally:
            sys.stdin = sys.__stdin__
            sys.stdout = sys.__stdout__
        return fake_frame.msg[0]

    def test_1(self):
       self.assertAlmostEqual(self.func_for_test('abababa', 'aba'),'3')

    def test_2(self):
       self.assertAlmostEqual(self.func_for_test('bbbbbb', 'aba'),'0')
       
    def test_3(self):
       self.assertAlmostEqual(self.func_for_test('aaa', 'a'),'3')

    def test_4(self):
        self.assertAlmostEqual(self.func_for_test('aba', '\n'),'4')




if __name__ == '__main__':
    unittest.main()


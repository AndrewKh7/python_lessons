import sys
import unittest
FILE = 'les33_task1.py'


class TestsForLes32Task2(unittest.TestCase):
    class FakeStream:
        def __init__(self, s):
            self.msg = []
            self.s = s
            self.gen = self.s_gen()

        def s_gen(self):
            yield self.s
            yield "@@@"

        def write(self,msg):
            self.msg.append(msg)

        def readline(self):
            return next(self.gen)

        def __iter__(self):
            return self.gen

    def func_for_test(self, s):
        fake_frame = self.FakeStream(s)
        try:
            sys.stdin = sys.stdout = fake_frame
            with open(FILE) as f:
                exec(f.read())
        finally:
            sys.stdin = sys.__stdin__
            sys.stdout = sys.__stdout__
        if fake_frame.msg:
            return fake_frame.msg[0]

    def test_1(self):
       self.assertEqual(self.func_for_test('cat'),None)

    def test_2(self):
       self.assertEqual(self.func_for_test(' catcat ' ),' catcat ')

    def test_3(self):
       self.assertEqual(self.func_for_test('Citty'),None)

    def test_4(self):
        self.assertEqual(self.func_for_test('cat cat '),'cat cat ')

    def test_5(self):
        self.assertEqual(self.func_for_test(' cat and cat '),' cat and cat ')


if __name__ == '__main__':
    unittest.main()


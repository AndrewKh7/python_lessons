import sys
import unittest



class TestsForLes32Task1(unittest.TestCase):
    class FakeStream:
        def __init__(self, s, a, b):
            self.msg = []
            self.s = s
            self.a = a
            self.b = b
            self.gen = self.s_gen()

        def s_gen(self):
            yield self.s
            yield self.a
            yield self.b

        def write(self,msg):
            self.msg.append(msg)

        def readline(self):
            return next(self.gen)

    def test_1(self):
        fake_frame = self.FakeStream('abababab', 'a', 'b')
        try:
            sys.stdin = sys.stdout = fake_frame
            with open('les32_task1.py') as f:
                exec(f.read())
            self.assertEqual('1',fake_frame.msg[0])
        finally:
            sys.stdin = sys.__stdin__
            sys.stdout = sys.__stdout__

    def test_2(self):
        fake_frame = self.FakeStream('\n', '\n', '\n')
        try:
            sys.stdin = sys.stdout = fake_frame
            with open('les32_task1.py') as f:
                exec(f.read())
            self.assertEqual('Impossible',fake_frame.msg[0])
        finally:
            sys.stdin = sys.__stdin__
            sys.stdout = sys.__stdout__
            

if __name__ == '__main__':
    unittest.main()


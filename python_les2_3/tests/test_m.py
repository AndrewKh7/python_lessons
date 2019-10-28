import sys
import unittest

class TestM(unittest.TestCase):
    class FakeStream:
        def __init__(self, readline_msg):
            self.msgs = []
            self.readline_msg = readline_msg


        def write(self, msg):
            self.msgs.append(msg)

        def readline(self):
            return self.readline_msg

    def test_1(self):
        fake_stream = self.FakeStream('6')
        try:
            sys.stdin = sys.stdout = fake_stream
            exec(open('m.py').read(), {'__name__' : '__main__'})
            self.assertEqual('3',fake_stream.msgs[0])
        finally:
            sys.stdin = sys.__stdin__
            sys.stdout = sys.__stdout__

    def test_2(self):
        fake_stream = self.FakeStream('Hello')
        try:
            with self.assertRaises(ValueError):
                sys.stdin = sys.stdout = fake_stream
                exec(open('m.py').read(), {'__name__' : '__main__'})
        finally:
            sys.stdin = sys.__stdin__
            sys.stdout = sys.__stdout__



if __name__ == '__main__':
    unittest.main()


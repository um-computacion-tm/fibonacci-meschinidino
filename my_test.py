import unittest

from fibonacci import fibonacci


class TestFib(unittest.TestCase):
    def test_caso_1(self):
        self.assertEqual(fibonacci(1), 1)

    def test_caso_2(self):
        self.assertEqual(fibonacci(2), 1)

    def test_caso_3(self):
        self.assertEqual(fibonacci(3), 2)

    def test_caso_4(self):
        self.assertEqual(fibonacci(4), 3)

    def test_caso_5(self):
        self.assertEqual(fibonacci(5), 5)

    def test_caso_15(self):
        self.assertEqual(fibonacci(15), 610)

    def test_caso_16(self):
        self.assertEqual(fibonacci(16), 987)

    def test_caso_17(self):
        self.assertEqual(fibonacci(17), 1597)

    def test_caso_18(self):
        self.assertEqual(fibonacci(18), 2584)

    def test_caso_19(self):
        self.assertEqual(fibonacci(19), 4181)

    def test_caso_20(self):
        self.assertEqual(fibonacci(20), 6765)


if __name__ == '__main__':
    unittest.main()

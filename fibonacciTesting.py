import unittest

class BaseFibonacci:
    def fibonacci(self, n):
        if n <= 0:
            return 0
        elif n == 1:
            return 1
        else:
            return self.fibonacci(n - 1) + self.fibonacci(n - 2)

class CheckFibonacci(BaseFibonacci):
    def testFibonacciSequence(self, num):
        return [self.fibonacci(i) for i in range(num)]

class TestFibonacci(unittest.TestCase):
    def setUp(self):
        self.fib = CheckFibonacci()

    def test_fibonacci(self):
        self.assertEqual(self.fib.fibonacci(0), 0)
        self.assertEqual(self.fib.fibonacci(1), 1)
        self.assertEqual(self.fib.fibonacci(2), 1)
        self.assertEqual(self.fib.fibonacci(3), 2)
        self.assertEqual(self.fib.fibonacci(4), 3)

    def testFibonacciSequence(self):
        self.assertEqual(self.fib.testFibonacciSequence(5), [0, 1, 1, 2, 3])

if __name__ == '__main__':
    unittest.main()




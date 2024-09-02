import unittest

class Parent:
    def multiply(self, x):
        return x * 2 

class Child(Parent):
    pass

class TestMultiply(unittest.TestCase):

    def test_multiply(self):
        child_instance = Child()
        self.assertEqual(child_instance.multiply(5), 10)  

    def test_multiply_again(self):
        child_instance_second = Child()
        self.assertEqual(child_instance_second.multiply(8), 16)  



if __name__ == '__main__':
    unittest.main()

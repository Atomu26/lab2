import unittest

class Parent:
    def division(self, x):
        return x / 2 
    def addition(self, y):
        return y + 2
    def subtraction(self, z):
        return z - 2 

class Child(Parent):
    pass

class TestMultiply(unittest.TestCase):

    def test_multiply(self):
        child_instance = Child()
        self.assertEqual(child_instance.multiply(10), 5.0)  

    def test_multiply_again(self):
        child_instance_second = Child()
        self.assertEqual(child_instance_second.multiply(16), 8.0) 
    def test_addition(self):
        child_instance_third = Child()
        self.assertEqual(child_instance_third.addition(5), 7)
    def test_subtraction(self):
        child_instance_third = Child()
        self.assertEqual(child_instance_third.subtraction(16), 14)



if __name__ == '__main__':
    unittest.main()

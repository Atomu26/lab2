 #Saleh Safi 

import unittest
class Parent:
     #First Method
    def square(self,p):
        return p*p
    #second one
    def times4(self,a):
        return a*4
class Child(Parent):
    pass

class TestMultiply(unittest.TestCase):

       # Testing find_max function
    def test_square(self):
        child_instance_fifth = Child()
        self.assertEqual(child_instance_fifth.square(2), 4)
      # Testing is_even function
    def test_times4(self):
        child_instance_sixth = Child()
        self.assertEqual(child_instance_sixth.times4(2), 8)

if __name__ == '__main__':
    unittest.main()



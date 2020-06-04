"""
**Unit testing

-testing smallest parts of an application is isolation(e.g. units)
-good candidates for unit testing: individual classes, modules, or functions 
-bad candidates for unit testing: an entire  application,dependencies across several classes or modules 

**unittest
-python comes with a built-in module called unitest
-you can write unit tests encapsulated as classes that inherit from unittest.TestCase

 to see verbose 

 python3 fileName.py -v
"""
import unittest
from activites import * 



class ActivityTests(unittest.TestCase):
    def test_eat_healthy(self):
        
        self.assertEqual(eat("broccoli", is_healthy=True),
        "I'm eating broccoli, because my body is  a temple")
    def test_eat_unhealthy(self):
        self.assertEqual(eat("pizza", is_healthy=False), "I'm eating pizza, because YOLO!")
    def test_short_nap(self):
        """ short naps should be refreshing"""
        self.assertEqual(nap(1), "I'm feeling refreshed after my 1 hour nap")
    def test_long_nap(self):
        """ long naps should be discouraging"""
        self.assertEqual(nap(3), "Ugh I overslept. I didn't mean to nap that long!")
    def test_is_funny_test(self):
        self.assertEqual(is_funny("tim"), False)
        # self.assertFalse(is_Funny("tim"), "tim should not be funny")
    def test_is_funny_anyone_else(self):
        """anyone else but tim should be funny"""
        self.assertTrue(is_funny("blue"), "blue should be funny")
        self.assertTrue(is_funny("tammy"), "tammy should be funny")
        self.assertTrue(is_funny("sven"), "sven should be funny")


if __name__ == "__main__":
    unittest.main()



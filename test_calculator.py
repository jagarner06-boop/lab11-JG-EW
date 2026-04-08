import unittest
from calculator import *

class TestCalculator(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(1, 2), 1+2)
        self.assertEqual(add(-5,944.6), -5+944.6)
        self.assertEqual(add(3.14159265,-036745.22),3.14159265+ -036745.22)

    def test_subtract(self):
        self.assertEqual(subtract(1, 2), 1-2)
        self.assertEqual(subtract(-5,944.6), -5-944.6)
        self.assertEqual(subtract(3.14159265,-036745.22),3.14159265-(-036745.22))

    ######## Partner 1
    def test_multiply(self): # 3 assertions
        self.assertAlmostEqual(mul(3,5),3*5)
        self.assertAlmostEqual(mul(3, 0), 3 * 0)
        self.assertAlmostEqual(mul(3, -1.2), 3 * -1.2)

    def test_divide(self): # 3 assertions
        self.assertAlmostEqual(div(3, 5), 5 / 3)
        self.assertAlmostEqual(div(-3, -1), -1 / -3)
        self.assertAlmostEqual(div(3, -1.2), -1.2 / 3)
    # ##########################

    def test_divide_by_zero(self): # 1 assertion
        with self.assertRaises(ZeroDivisionError):
            div(0,5)

    def test_logarithm(self): # 3 assertions
        self.assertAlmostEqual(logarithm(2,4), math.log(4,2))
        self.assertAlmostEqual(logarithm(65, 9), math.log(9, 65))
        self.assertAlmostEqual(logarithm(5, 42), math.log(42, 5))


    def test_log_invalid_base(self): # 1 assertion
        with self.assertRaises(ValueError):
            logarithm(-6,-5)

    ######## Partner 1
    def test_log_invalid_argument(self): # 1 assertion
    #     # call log function inside, example:
    #     # with self.assertRaises(<INSERT_ERROR_TYPE>):
    #     #     logarithm(0, 5)
    #     fill in code
        with self.assertRaises(ValueError):
            logarithm(0,5)

    def test_hypotenuse(self): # 3 assertions
        self.assertAlmostEqual(hypotenuse(3,4),5)
        self.assertAlmostEqual(hypotenuse(8,6),10)
        self.assertAlmostEqual(hypotenuse(3, 5), (3**2+5**2)**0.5)

    def test_sqrt(self): # 3 assertions
    #     # Test for invalid argument, example:
         with self.assertRaises(ValueError):
            square_root(-1)
    #     # Test basic function
    #     fill in code
    ##########################

# Do not touch this
if __name__ == "__main__":
    unittest.main()
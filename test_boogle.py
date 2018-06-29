import unittest
import boogle

"""
The unittest framework uses classes and inheritance so we'll create a class 
that inherits from the test framework and then we'll write the methods inside 
the actual class
"""

#We wrote a test to make sure this was working but this is not the test we
#need so we'll deleted (commented) and instead make sure we're importing the
#file we really need to test, in this case boogle (see above)
# class test_boogle(unittest.TestCase):
#     def test_is_this_thing_on(self):
#         self.assertEqual(1, 1)

#Here we create the class inheriting from testCase
#This is out test suit for Boogle Solver

class TestBoogle(unittest.TestCase):
    
    def test_can_create_an_empty_grid(self):
        """
        Test to see if we can create an empty grid
        """
        grid = boogle.make_grid(0,0)
        self.assertEqual(len(grid),0)
        #The assertion is that a 0 x 0 grid has a length of 0
    
    def test_grid_size_is_width_times_height(self):
        """
        Test is to ensure that the total size of the grid is equal to 
        width * height
        """
        grid = boogle.make_grid(2, 3)
        self.assertEqual(len(grid), 6)
        #The assertion means that if grid length is 2*3, we'd expect it to be
        #equal to 6
    
    def test_grid_coordinates(self):
        """
        Test to ensure that all of the coordinates inside of the grid can be
        accessed
        """
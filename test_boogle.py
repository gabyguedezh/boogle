import unittest
import boogle
from string import ascii_uppercase #The 26 ascii uppercase characters A to Z

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
        grid = boogle.make_grid(2, 2)
        #We use the assertIn method to check whether 0,0 IS IN a 2x2 grid
        self.assertIn((0, 0), grid)
        #We check the same for (0, 1), (1, 0) and for (1, 1)
        self.assertIn((0, 1), grid)
        self.assertIn((1, 1), grid)
        #The assertNotIn method asserts that (2, 2) IS NOT in a 2x2 grid
        self.assertNotIn((2, 2), grid)
    
    def test_grid_is_filled_with_letters(self):
        """
        Ensure that each of the coordinates of the grid contains letters
        """
        #Initially this test will fail because at the point of writing, our 
        #grid is filled with spaces as specified in the tuple we've created
        grid = boogle.make_grid(2, 3)
        for letter in grid.values(): 
        #Remember our tupple with key: row-col, value: ("should be letter")
            self.assertIn(letter, ascii_uppercase)
            #This test to see if our "letter" is one of the 26 ascii characters
    
    def test_neighbours_of_a_position(self):
        """
        Ensure that a position has 8 neighbours (while we know this won't be the
        case if it's on an edge or a corner, we're not concerned with those 
        special cases yet)
        """
        coords = (1, 2)
        neighbours = boogle.neighbours_of_position(coords)
        self.assertIn((0, 1), neighbours)
        self.assertIn((0, 2), neighbours)
        self.assertIn((0, 3), neighbours)
        self.assertIn((1, 1), neighbours)
        self.assertIn((1, 3), neighbours)
        self.assertIn((2, 1), neighbours)
        self.assertIn((2, 2), neighbours)
        self.assertIn((2, 3), neighbours)
        #We're writing very simple code which we can turn complex later on 
        #Is easier to make simple complex than to make complex simple
        #We want to test if there are neighbours in a given coordinate
    
    def test_all_neighbours_grid(self):
        """
        Ensure that all of the grid positions have neighbours.
        The trick is to remember that in a 2x2 grid, every position touches 
        #every other position, so the neighbours of any position are the other
        #three positions of the 2x2 grid
        """
        #We make a 2x2 grid for testing purposes
        grid = boogle.make_grid(2, 2)
        #In the line below, we get all the neighbours for the grid.
        #This is a dictionary where the key is a position (just like with the
        #grid itself) and the VALUE is a list of neighbouring positions
        neighbours = boogle.all_grid_neighbours(grid)
        #The next line asserts the correct length of the neighbours dictionary
        self.assertEqual(len(neighbours), len(grid))
        #The FOR loop will iterate through the positions in the grid. 
        for pos in grid:
            #For each position, the neighbours are the other three positions on
            #the grid, so we create the OTHERS list, which is a full grid minus 
            #the position in question
            others = list(grid) #Creates a new list from the dictionary's keys
            others.remove(pos) #Removes a given position, leaving only neighbours
            #It asserts that the positions are the neighbours of the position
            #being checked. Remember that in a 2x2, the neigbours list should be
            #equal to a list of all the positions minus the given one (others)
            self.assertListEqual(sorted(neighbours[pos]), sorted(others))

    #Now we'll create our words    
    def test_cenverting_a_path_to_a_word(self):
        """
        A word is generated by following a path through the grid.
        This function ensures the paths can be converted to words.
        We could create a specific grid with specific letters but there's no
        need for that yet as at this point the actual letters don't matter
        """
        grid = boogle.make_grid(2, 2)
        #We can access a letter in the grid by its position, in this case [0, 0]
        oneLetterWord = boogle.path_to_word(grid, [(0, 0)])
        twoLetterWord = boogle.path_to_word(grid, [(0, 0), (1, 1)])
        #This tests checks that the path_to_word function returns the same
        #string we manually constructed in the test
        self.assertEqual(oneLetterWord, grid[(0, 0)])
        self.assertEqual(twoLetterWord, grid[(0,0)] + grid[(1, 1)])
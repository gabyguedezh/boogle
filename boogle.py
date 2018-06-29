from string import ascii_uppercase #The 26 ascii uppercase characters A to Z
from random import choice

def make_grid(width, height):
    # """
    # Make an empty Boogle grid
    # """
    #First, we'll return an empty grid to check if our test passes (at this 
    #point, out test is expecting an empty grid to test if its length equals 0)
    #return {}
    
    #After that, we move to create a grid with actual width and height (we've 
    #previously built the test to ensure it will work on the other .py)
    
    # """
    # Creates a grid that will hold all of the tiles for a boogle game
    # This function creates a dictionary with a row-column tuple as the key
    # and a space as the value (we're not concern yet with the letter)
    # """
    # return {(row, col): " " for row in range(height)
    #     for col in range(width)}
    
    """
    Once we got our grid and we imported ascii_uppercase characters, we can
    add the letters to our grid. We'll use the CHOICE method from the RANDOM
    module to randomise the letters in our coordinates
    """
    return {(row, col): choice(ascii_uppercase) for row in range(height)
        for col in range(width)
    }

#Now we create a new function
def neighbours_of_position(coords):
    """
    Get neighbours of a given position
    """
    #First, we just assign a number to each variable
    row = coords[0] 
    col = coords[1]
    
    #Assign each of the neighbours 
    #Top left to top right
    top_left = (row - 1, col - 1)
    top_center = (row - 1, col)
    top_right = (row - 1, col + 1)
    
    #Left to right
    left = (row, col - 1)
    #The row-col coordinates passed to this function are here (row, col)
    right = (row, col + 1)
    
    #Bottom-left to bottom-right
    bottom_left = (row + 1, col - 1)
    bottom_center = (row + 1, col)
    bottom_right = (row + 1, col + 1)
    
    return [top_left, top_center, top_right,
            left, right,
            bottom_left, bottom_center, bottom_right]

def all_grid_neighbours(grid):
    """
    Gets all of the posible neighbours for each position in the grid
    """
    neighbours = {}
    for position in grid:
        position_neighbours = neighbours_of_position(position)
        neighbours[position] = [p for p in position_neighbours if p in grid]
    return neighbours
   

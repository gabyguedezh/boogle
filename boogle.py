def make_grid(width, height):
    # """
    # Make an empty Boogle grid
    # """
    #First, we'll return an empty grid to check if our test passes (at this 
    #point, out test is expecting an empty grid to test if its length equals 0)
    #return {}
    
    #After that, we move to create a grid with actual width and height (we've 
    #previously built the test to ensure it will work on the other .py)
    
    """
    Creates a grid that will hold all of the tiles for a boogle game
    This function creates a dictionary with a row-column tuple as the key
    and a space as the value
    """
    return {(row, col): " " for row in range(height)
        for col in range(width)}
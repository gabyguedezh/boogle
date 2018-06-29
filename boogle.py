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
    #neighbours = {} is creating an empty dictionary so you have somewhere to 
    #store the neighbours of all the grid positions. 
    neighbours = {}
    #Remember, we use a dictionary if we want key value pairs. In this case you
    #need to know which neighbour and what letter it contains so a dictionary 
    #is the best way to capture this.
    for position in grid:
        position_neighbours = neighbours_of_position(position)
        neighbours[position] = [p for p in position_neighbours if p in grid]
        #Here we are adding the position to the dictionary but only those 
        #neighbours that are actually in the grid. 
        #So a corner or edge grid position has neighbours that are outside the
        #grid but we don't care about them as they cannot contain a letter. 
    return neighbours
    
#Now we create our word generator
def path_to_word(grid, path):
    """
    Adds all of the letters on a path to a string
    """
    #This gets the list of letters for the positions in the path and then joins
    #them into a string (join positions of grid if they're in the path)
    return "".join([grid[p] for p in path])

#Now we create a serach function
def search(grid, dictionary):
    """
    This function accepts a grid and a dictionary, so it matches the 
    dependencies we've identified early on.
    We search through the path to locate the words by matching strings to the
    words in a dictionary (so, if the string is not equal to a word in the 
    dictionary, it won't be a valid word for our game)
    """
    #first we get the neighbours of every position in the grid, and then we get
    #the paths list to capture all paths that form valid words
    neighbours = all_grid_neighbours(grid)
    paths = []
    #The reason why we're storing words as paths rather than as strings is that 
    #a letter can be repeated in the grid several times (if we had two letter "A"
    #and we saved a word with an "A" in it, the program woudln't know which "A" 
    #was it)
    
    def do_search(path):
        #It is perfectly valid to nest functions and in this case it will be 
        #useful. The do_search function exists within the scope of the search()
        #function (it can't be called directly).
        #The search() function starts to search by passing a single position to
        #the do_search(). This is a path of one letter. 
        word = path_to_word(grid, path)
        #The do_search function has access to the other variables defined within
        #the search(), such as the path list, which it can add to.
        #The do_search function converts whatever path that's given into a word 
        #and checks if it's in the dictionary.
        if word in dictionary:
            #If the path makes a word, it's added to the paths list.
            paths.append(path)
        #The do_search function can be called by the search() function, and it can
        #call itself recursively to build up paths.
        for next_pos in neighbours[path[- 1]]:
            if next_pos not in path:
                do_search(path + [next_pos])
        #Whether the path makes a word or not, do_search gets each of the 
        #neighbours of the last letter, checks to make sure the neighbouring
        #letter isn't already in the path, and then continues the searching
        #from that letter
        #So, do_search calls itself eight time for each starting position, and
        #again and again for each of the various neighbours of each neighbour
    
    for position in grid:
        do_search([position])
        
    words = []
    
    for path in paths:
        words.append(path_to_word(grid, path))
    return set(words)
    #For each position in the grid we do a search and convert all the paths and
    #make valid words into words and return them in a list
    
  

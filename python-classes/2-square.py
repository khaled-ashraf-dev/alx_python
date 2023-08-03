"""
A class representing a square.
"""

class Square:
    """
        Constructor for the Square class.

        Parameters:
        size (int): The size of the square's side.

        Initializes a new Square object with the specified size.
        The size is assigned to the private instance variable __size.
        """
    def __init__(self, size=0):
        """
        Constructor for the Square class.

        Parameters:
        size (int): The size of the square's side.

        Initializes a new Square object with the specified size.
        The size is assigned to the private instance variable __size.
        """
        self.__size = size
        if not isinstance(self.__size, int):
            raise TypeError('size must be an integer')
        
        if self.__size < 0:
            raise ValueError('size must be >= 0')
    
    def area(self):
        return self.__size ** 2
from base import Base

"""
    Represents a base entity.

    Attributes:
        __nb_objects (int): A private class-level attribute to track the number of objects created.
        Represents a base entity.

    Attributes:
        __nb_objects (int): A private class-level attribute to track the number of objects created.
        Represents a base entity.

    Attributes:
        __nb_objects (int): A private class-level attribute to track the number of objects created.
"""
class Rectangle(Base):
    """
        Represents a base entity.

        Attributes:
            __nb_objects (int): A private class-level attribute to track the number of objects created.
            Represents a base entity.

        Attributes:
            __nb_objects (int): A private class-level attribute to track the number of objects created.
            Represents a base entity.

        Attributes:
            __nb_objects (int): A private class-level attribute to track the number of objects created.
    """
    def __init__(self):
        """
        Initializes an instance of the Base class.

        Args:
            id (int): An optional identifier to assign to the instance.
        Initializes an instance of the Base class.

        Args:
            id (int): An optional identifier to assign to the instance.
        """
        super().__init__()  # Call the constructor of the parent class
    
    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Initializes an instance of the Base class.

        Args:
            id (int): An optional identifier to assign to the instance.
        Initializes an instance of the Base class.

        Args:
            id (int): An optional identifier to assign to the instance.
        """
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
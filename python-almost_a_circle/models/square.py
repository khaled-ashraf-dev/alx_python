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
from models.rectangle import Rectangle

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
class Square(Rectangle):
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
    def __init__(self, size, x=0, y=0, id=None):
        """
            Represents a base entity.

            Attributes:
                __nb_objects (int): A private class-level attribute to track the number of objects created.
                Represents a base entity.
        """    
        super().__init__(size, size, x, y, id)  # Call the super class with id
        self.width = size
        self.height = size
    def __str__(self):
        """
            Represents a base entity.

            Attributes:
                __nb_objects (int): A private class-level attribute to track the number of objects created.
                Represents a base entity.
        """

        return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y, self.width)
    
    @property
    def size(self):
        """
            Represents a base entity.

            Attributes:
                __nb_objects (int): A private class-level attribute to track the number of objects created.
                Represents a base entity.
        """
        return self.width
    
    @size.setter
    def size(self, value):
        """
            Represents a base entity.

            Attributes:
                __nb_objects (int): A private class-level attribute to track the number of objects created.
                Represents a base entity.
        """
        self.width = value
        self.height = value
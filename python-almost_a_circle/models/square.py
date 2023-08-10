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
        super().__init__(size, size, x, y, id)  # Call the super class with id
        self.width = size
        self.height = size

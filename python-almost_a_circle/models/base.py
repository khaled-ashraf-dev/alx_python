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

class Base:
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

    __nb_objects = 0
    
    def __init__(self, id=None):
        """
        Initializes an instance of the Base class.

        Args:
            id (int): An optional identifier to assign to the instance.
        Initializes an instance of the Base class.

        Args:
            id (int): An optional identifier to assign to the instance.
        """
        if id is not None:
            self.id = id

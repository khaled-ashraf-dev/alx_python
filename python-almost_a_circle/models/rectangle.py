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
from models.base import Base

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
    def __init__(self, width, height, x=0, y=0, id=None):
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
        super().__init__(id)  # Call the super class with id
        self.width = width
        self.height = height
        self.x = x
        self.y = y
    
    # Getter and Setter for width
    @property
    def width(self):
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
        return self.__width
    
    @width.setter
    def width(self, value):
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
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value
    
    # Getter and Setter for height
    @property
    def height(self):
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
        return self.__height
    
    @height.setter
    def height(self, value):
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
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value
    
    # Getter and Setter for x
    @property
    def x(self):
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
        return self.__x
    
    @x.setter
    def x(self, value):
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
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value
    
    # Getter and Setter for y
    @property
    def y(self):
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
        return self.__y
    
    @y.setter
    def y(self, value):
        """
            Represents a base entity.

            Attributes:
                __nb_objects (int): A private class-level attribute to track the number of objects created.
                Represents a base entity.

        """
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """
        Represents a base entity.

            Attributes:
                __nb_objects (int): A private class-level attribute to track the number of objects created.
                Represents a base entity.
        """
        return self.height * self.width
    
    def display(self):
        """
        Represents a base entity.

            Attributes:
                __nb_objects (int): A private class-level attribute to track the number of objects created.
                Represents a base entity.
        """
        for i in range(self.y):
            print()
        for i in range(self.height):
            print(' ' * self.x + '#' * self.width)
    
    def __str__(self) -> str:
        """
        Represents a base entity.

            Attributes:
                __nb_objects (int): A private class-level attribute to track the number of objects created.
                Represents a base entity.
        """
        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id, self.x, self.y, self.width, self.height)
    
    def update(self, *args, **kwargs):
        """
        Represents a base entity.

            Attributes:
                __nb_objects (int): A private class-level attribute to track the number of objects created.
                Represents a base entity.
        """
        if args:
            try:
                self.id = args[0]
            except:
                pass
            
            try:
                self.width = args[1]
            except:
                pass

            try:
                self.height = args[2]
            except:
                pass

            try:
                self.x = args[3]
            except:
                pass

            try:
                self.y = args[4]
            except:
                pass
        else:
            if 'id' in kwargs:
                self.id = kwargs['id']
            if 'height' in kwargs:
                self.height = kwargs['height']
            if 'width' in kwargs:
                self.width = kwargs['width']
            if 'x' in kwargs:
                self.x = kwargs['x']
            if 'y' in kwargs:
                self.y = kwargs['y']
        
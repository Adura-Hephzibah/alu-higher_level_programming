#!/usr/bin/python3
"""
contains class Square
inherits from class Rectangle
"""


from models.rectangle import Rectangle


class Square(Rectangle):
    """defines class Square"""
    def __init__(self, size, x=0, y=0, id=None):
        """initialization"""
        super().__init__(size, size, x, y, id)
        self.size = size

    @property
    def size(self):
        """Getter size"""
        return self.width

    @size.setter
    def size(self, value):
        """Setter size - sets width and height as size"""
        self.width = value
        self.height = value

    def __str__(self):
        """prints [Square] (<id>) <x>/<y> - <size>"""
        return "[{:s}] ({:d}) {:d}/{:d} - {:d}".format(
                self.__class__.__name__, self.id, self.x, self.y,
                self.size)

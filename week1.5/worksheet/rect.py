# Worksheet 1.5: Rectangle Class

class Rectangle:
    """
    A rectangle, with a width and a height.
    """
    def __init__(self, width, height):
        """
        Creates a Rectangle, given values for width and height.
        """
        if not isinstance(width, int) or not isinstance(height, int):
            raise TypeError()

        if width <= 0 or height <= 0 :
            raise ValueError()
        
        self.width = width
        self.height = height

    # Implement methods is_square(), area() & perimeter() here
    def is_square (self) :
        if self.height == self.width :
            return True
        else :
            return False

    def area (self) :
        return self.width * self.height

    def perimeter (self) :
        return (2 * self.width) + (2 * self.height)
    
    # (See README.md for details of what they should do)

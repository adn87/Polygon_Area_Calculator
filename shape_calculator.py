class Rectangle:
  def __init__(self, width, height):
    self.width = width
    self.height = height

  def __str__(self):
    width = str(self.width)
    height = str(self.height)
    return 'Rectangle(width=' + width + ', height=' + height + ')'

  def set_width(self, width):
    self.width = width

  def set_height(self, height):
    self.height = height

  def get_area(self):
    return self.width * self.height

  def get_perimeter(self):
    return (2* (self.width + self.height))

  def get_diagonal(self):
    return (self.width ** 2 + self.height ** 2) ** 0.5

  def get_picture(self):
    if self.width > 50 or self.height > 50:
      return 'Too big for picture.'
    else:
      return ("*" * self.width + "\n") * self.height

  def get_amount_inside(self, shape):
    in_width = self.width // shape.width
    in_height = self.height // shape.height
    return in_width * in_height

class Square(Rectangle):
  def __init__(self, side):
    super().__init__(side,side)

  def __str__(self):
    return f'{type(self).__name__}(side={self.width})'

  def set_side(self, side):
    self.set_width(side)
    self.set_height(side)

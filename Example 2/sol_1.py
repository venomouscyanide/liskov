# sol 1. Don't use inheritance at all.


class Rectangle:
    def __init__(self):
        self._height = 0
        self._width = 0

    @property
    def height(self):
        return self._height

    @property
    def width(self):
        return self._width

    @height.setter
    def set_height(self, height):
        self._height = height

    @width.setter
    def set_width(self, width):
        self._width = width

    def calculate_area(self):
        return self._height * self._width


class Square():
    def __init__(self):
        self._side = 0

    @property
    def side(self):
        return self._side

    @side.setter
    def set_side(self, side):
        self._side = side

    def calculate_area(self):
        return pow(self._side, 2)


def main():
    rectangle = Rectangle()
    rectangle.set_height = 5
    rectangle.set_width = 10
    print(rectangle.calculate_area())

    square = Square()
    square.set_side = 5
    print(square.calculate_area())


if __name__ == '__main__':
    main()

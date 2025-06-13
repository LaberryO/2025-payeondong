class Screen:
    def __init__(self, width, height):
        self._width = width
        self._height = height

    @property
    def width(self):
        return self._width
    
    @width.setter
    def width(self, value):
        if value > 0:
            self._width = value
        else:
            Exception.ValueException("Screen의 width가 올바르지 않습니다.")
    
    @property
    def height(self):
        return self._height
    
    @height.setter
    def height(self, value):
        if value > 0:
            self._height = value
        else:
            Exception.ValueException("Screen의 height가 올바르지 않습니다.")

    @property
    def size(self):
        return (self._width, self._height)

    @property
    def center_x(self):
        return self._width / 2
    
    @property
    def center_y(self):
        return self._height / 2
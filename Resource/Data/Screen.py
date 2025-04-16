class Screen:
    def __init__(self):
        self.width = 1600;
        self.height = 900;

    # Getter
    def getWidth(self):
        return self.width;

    def getHeight(self):
        return self.height;

    def getSize(self):
        return self.getWidth(), self.getHeight();

    def getCenterX(self):
        return self.width / 2;

    def getCenterY(self):
        return self.height / 2;

    # Setter
    def setWidth(self, width):
        self.width = width;
    
    def setHeight(self, height):
        self.height = height;

    def setSize(self, width, height):
        self.setWidth(width);
        self.setHeight(height);
    
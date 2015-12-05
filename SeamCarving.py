import matplotlib.image as mpli

class SeamCarver:
    # an RGB 2d array
    m_data = None
    row = 0
    col = 0
    
    
    def __init__(self, imagePath):
        self. m_data = mpli.imread(imagePath)
        self.row = len(self.m_data)
        self.col = len(self.m_data[0])

    # returns energy of specified pixel
    def energy(self, x, y):
        # TODO: edge cases
        return self._gradientSquareX(x, y)**2 + self._gradientSquareY(x, y)**2
        
    def _gradientSquareX(self, x, y):
        # Rx(x, y), Gx(x, y), and Bx(x, y) are the absolute value in differences
        # of red, green, and blue components between pixel (x + 1, y) and pixel (x − 1, y)

        # TODO: edge cases
        Rx = int(self.m_data[x + 1][y][0]) - int(self.m_data[x - 1][y][0])
        Gx = int(self.m_data[x + 1][y][1]) - int(self.m_data[x - 1][y][1])
        Bx = int(self.m_data[x + 1][y][2]) - int(self.m_data[x - 1][y][2])

        return Rx**2 + Gx**2 + Bx**2
    
    def _gradientSquareY(self, x, y):
        # Ry(x, y), Gy(x, y), and By(x, y) are the absolute value in differences
        # of red, green, and blue components between pixel (x, y + 1) and pixel (x, y - 1)

        # TODO: edge cases
        Ry = int(self.m_data[x][y + 1][0]) - int(self.m_data[x][y - 1][0])
        Gy = int(self.m_data[x][y + 1][1]) - int(self.m_data[x][y - 1][1])
        By = int(self.m_data[x][y + 1][2]) - int(self.m_data[x][y - 1][2])

        return Ry**2 + Gy**2 + By**2

    
    # returns an array of row indices for a horizontal seam
    def horizontalSeam():
        # TODO

    # returns an array of column indices for a vertical seam
    def verticalSeam():
        # TODO

    # seam is a 2D array
    def removeVertical(seam):
        # TODO
        
    # seam is a 2D array
    def removeHorizontal(seam):
        # TODO

    # removes seams corresponding to the difference in dimensions
    def scaleDown(newLength, newWidth):
        # TODO


s = SeamCarver("images/example_1.jpg")
#print("2, 2: " + s.m_data[2][2])
e_test = s.energy(2,2)
print(e_test)
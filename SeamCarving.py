import matplotlib.image as mpli

class SeamCarver:
    # an RGB 2d array
    m_data = None
    row = 0
    col = 0
    
    
    def __init__(self, imagePath):
        self. m_data = mpli.imread(imagePath)
        self.row = len(m_data)
        self.col = len(m_data[0])

    # returns energy of specified pixel
    def energy(x, y):
        # TODO: edge cases
        return _gradientSquareX(x, y)**2 + _gradientSquareY(x, y)**2
        
    def _gradientSqaureX(x, y):
        # Rx(x, y), Gx(x, y), and Bx(x, y) are the absolute value in differences
        # of red, green, and blue components between pixel (x + 1, y) and pixel (x − 1, y)

        # TODO: edge cases
        Rx = m_data[x + 1][y][0] - m_data[x - 1][y][0]
        Gx = m_data[x + 1][y][1] - m_data[x - 1][y][1]
        Bx = m_data[x + 1][y][2] - m_data[x - 1][y][2]

        return Rx**2 + Gx**2 + Bx**2
    
    def _gradientSqaureY(x, y):
        # Ry(x, y), Gy(x, y), and By(x, y) are the absolute value in differences
        # of red, green, and blue components between pixel (x, y + 1) and pixel (x, y - 1)

        # TODO: edge cases
        Ry = m_data[x][y + 1][0] - m_data[x][y - 1][0]
        Gy = m_data[x][y + 1][1] - m_data[x][y - 1][1]
        By = m_data[x][y + 1][2] - m_data[x][y - 1][2]

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

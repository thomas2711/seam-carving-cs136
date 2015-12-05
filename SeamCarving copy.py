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
        horizontal = {}
        min = 0
        minEnergy = energy(0, 0)
        for i in range (1, self.height):
            temp = energy(0, i)
            if minEnergy > temp:
                minEnergy = temp
                min = i
        horizontal.append(min)
        for i in range (0, self.width - 1):
            horizontal.append(_findHoriIndex(i, min))

        return horizontal

    
    def _findHoriIndex(x, y):
        e1 = energy(x + 1, y - 1)
        e2 = energy(x + 1, y)
        e3 = energy(x + 1, y + 1)
        min = y - 1
        minEnergy = e1
        if minEnergy > e2:
            minEnergy = e2
            min = y
        if minEnergy > e3:
            min = y + 1

        return min

    # returns an array of column indices for a vertical seam
    def verticalSeam():
        # TODO
        vertical = {}
        min = 0
        minEnergy = energy(0, 0)
        for i in range (1, self.width):
            temp = energy(i, 0)
            if minEnergy > temp:
                minEnergy = temp
                min = i
        vertical.append(min)
        for i in range (0, self.height - 1):
            vertical.append(_findVertiIndex(min, i))

        return vertical
    
    def _findVertiIndex(x, y):
        e1 = energy(x - 1, y + 1)
        e2 = energy(x, y + 1)
        e3 = energy(x + 1, y + 1)
        min = x - 1
        minEnergy = e1

        if minEnergy > e2:
            minEnergy = e2
            min = x
        if minEnergy > e3:
            min = x + 1

        return min


    # seam is a 2D array
    def removeVertical(seam):
        # TODO
        
    # seam is a 2D array
    def removeHorizontal(seam):
        # TODO

    # removes seams corresponding to the difference in dimensions
    def scaleDown(newLength, newWidth):
        # TODO

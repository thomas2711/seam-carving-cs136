import matplotlib.image as mpli

class SeamCarver:
    # an RGB 2d array
    m_data = None
    row = 0
    col = 0
    
    
    def __init__(self, imagePath):
        self.m_data = mpli.imread(imagePath)
        self.row = len(self.m_data)
        self.col = len(self.m_data[0])


    # returns energy of specified pixel
    def energy(self, x, y):
        # TODO: edge cases
        return self._gradientSquareX(x, y) + self._gradientSquareY(x, y)
        
    def _gradientSquareX(self, x, y):
        # Rx(x, y), Gx(x, y), and Bx(x, y) are the absolute value in differences
        # of red, green, and blue components between pixel (x + 1, y) and pixel (x − 1, y)

        # TODO: edge cases
        Rx = int(self.m_data[y][(x + 1) % self.col][0]) - int(self.m_data[y][x - 1][0])
        Gx = int(self.m_data[y][(x + 1) % self.col][1]) - int(self.m_data[y][x - 1][1])
        Bx = int(self.m_data[y][(x + 1) % self.col][2]) - int(self.m_data[y][x - 1][2])
        
        return Rx**2 + Gx**2 + Bx**2
    
    def _gradientSquareY(self, x, y):
        # Ry(x, y), Gy(x, y), and By(x, y) are the absolute value in differences
        # of red, green, and blue components between pixel (x, y + 1) and pixel (x, y - 1)

        # TODO: edge cases
        Ry = int(self.m_data[(y + 1) % self.row][x][0]) - int(self.m_data[y - 1][x][0])
        Gy = int(self.m_data[(y + 1) % self.row][x][1]) - int(self.m_data[y - 1][x][1])
        By = int(self.m_data[(y + 1) % self.row][x][2]) - int(self.m_data[y - 1][x][2])

        return Ry**2 + Gy**2 + By**2

    
    # returns an array of row indices for a horizontal seam
    def horizontalSeam(self):
        # TODO
        horizontal = []
        min = 0
        minEnergy = self.energy(0, 0)
        for i in range (1, self.row):
            temp = self.energy(0, i)
            if minEnergy > temp:
                minEnergy = temp
                min = i
        horizontal.append(min)
        for i in range (0, self.col - 1):
            horizontal.append(self._findHoriIndex(i, min))

        return horizontal

    
    def _findHoriIndex(self, x, y):
        e1 = self.energy(x + 1, y - 1)
        e2 = self.energy(x + 1, y)
        e3 = self.energy(x + 1, y + 1)
        min = y - 1
        minEnergy = e1
        if minEnergy > e2:
            minEnergy = e2
            min = y
        if minEnergy > e3:
            min = y + 1

        return min

    # returns an array of column indices for a vertical seam
    def verticalSeam(self):
        # TODO
        vertical = []
        min = 0
        minEnergy = self.energy(0, 0)
        for i in range (1, self.col):
            temp = self.energy(i, 0)
            if minEnergy > temp:
                minEnergy = temp
                min = i
        vertical.append(min)
        for i in range (0, self.row - 1):
            vertical.append(self._findVertiIndex(min, i))

        return vertical
    
    def _findVertiIndex(self, x, y):
        e1 = self.energy(x - 1, y + 1)
        e2 = self.energy(x, y + 1)
        e3 = self.energy(x + 1, y + 1)
        min = x - 1
        minEnergy = e1

        if minEnergy > e2:
            minEnergy = e2
            min = x
        if minEnergy > e3:
            min = x + 1

        return min
    
    def markVerticalSeam(self):
        seam = self.verticalSeam()
        for i in range (0, self.row):
            self.m_data[seam[i]][i][0] = 255
            self.m_data[seam[i]][i][1] = 0
            self.m_data[seam[i]][i][2] = 0

    def markHorizontalSeam(self):
        seam = self.horizontalSeam()
        for i in range (0, self.col):
            self.m_data[i][seam[i]][0] = 255
            self.m_data[i][seam[i]][1] = 0
            self.m_data[i][seam[i]][2] = 0
    
#    # seam is a 2D array
#    def removeVertical(self, seam):
#        # TODO
#        
#    # seam is a 2D array
#    def removeHorizontal(self, seam):
#        # TODO
#
#    # removes seams corresponding to the difference in dimensions
#    def scaleDown(self, newLength, newWidth):
#        # TODO


s = SeamCarver("images/example_1.jpg")
#print("2, 2: " + s.m_data[2][2])
#e_test = s.energy(0,1)
#print(e_test)
s.markVerticalSeam()
mpli.imsave("test.jpg", s.m_data)
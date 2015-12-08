import matplotlib.image as mpli
import math
import numpy as np


class SeamCarver:
    # an RGB 2d array
    m_data = None
    row = 0
    col = 0
    energyMap = None
    
    
    def __init__(self, imagePath):
        self.m_data = mpli.imread(imagePath)
        self.row = len(self.m_data)
        self.col = len(self.m_data[0])
        
        #t = np.array(dtype=np.float32)
    
        for x in range (0, self.row):
            for i in range (0, self.col):
                z = self.energy(i, x)
                a = int((float(z)/625.0)*255.0)
                if a < 127:
                    a = np.uint8(0)
                else:
                    a = np.uint8(255)
                b = np.array([a, a, a], dtype=np.uint8)
                self.m_data[x][i] = b
                self.m_data[x][i][0] = a
                self.m_data[x][i][1] = a
                self.m_data[x][i][2] = a
    
    
    # returns energy of specified pixel
    def energy(self, x, y):
        # TODO: edge cases
        # return math.sqrt(self._gradientSquareX(x, y) + self._gradientSquareY(x, y))
      #  a = 0 if x == 0 or y == 0 else self.brightness(x - 1, y - 1)
  #      b = 0 if y == 0 else self.brightness(x, y - 1)
   #     c = 0 if y == 0 or x == self.col - 1 else self.brightness(x + 1, y - 1)
    #    d = 0 if x == 0 else self.brightness(x - 1, y)
     #   e = self.brightness(x, y)
      #  f = 0 if x == self.col - 1 else self.brightness(x + 1, y)
       # g = 0 if x == 0 or y == self.row - 1 else self.brightness(x - 1, y + 1)
        #h = 0 if y == self.row - 1 else self.brightness(x, y + 1)
        #i = 0 if x == self.col - 1 or y == self.row - 1 else self.brightness(x + 1, y + 1)
        #xenergy = a + 2 * d + g - c - 2 * f - i
        #yenergy = a + 2 * b + c - g - 2 * h - i
        #return math.sqrt(xenergy**2 + yenergy**2)
        return math.sqrt((self.rgb2gray(x - 1, y) - self.rgb2gray((x + 1) % self.col, y))**2 + (self.rgb2gray(x, y - 1) - self.rgb2gray(x, (y + 1) % self.row))**2)
    
    def generateEMap(self):
        self.energyMap = []
        for i in range (0, self.row):
            self.energyMap.append([])
            for j in range (0, self.col):
                self.energyMap[i].append(self.energy(j, i))

        
    def rgb2gray(self, x, y):
        return 0.2989 * (int)(self.m_data[y][x][0]) + 0.5870 * (int)(self.m_data[y][x][1]) + 0.1140 * (int)(self.m_data[y][x][2])
        
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

    def brightness(self, x, y):
        return (int)(self.m_data[y][x][0]) + (int)(self.m_data[y][x][1]) + (int)(self.m_data[y][x][2])
    
    
    
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
            #temp = min
            min = self._findHoriIndex(i, min)
            horizontal.append(min)

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

    
    def markVerticalSeam(self):
        seam = self.findVSeam()
        for i in range (0, self.row):
            self.m_data[i][seam[i]][0] = 255
            self.m_data[i][seam[i]][1] = 0
            self.m_data[i][seam[i]][2] = 0

    def markHorizontalSeam(self):
        seam = self.findHSeam()
        for i in range (0, self.col):
            self.m_data[seam[i]][i][0] = 255
            self.m_data[seam[i]][i][1] = 0
            self.m_data[seam[i]][i][2] = 0

    # scoring matrix M
   
    def scoringHorizontal(self):
        # 0th col remains the same
        for col in range (1, self.col):
            M[0][col] += min(M[0][col - 1], M[1][col - 1])
            for row in range (1, self.row - 1):
                M[row][col] += min(M[row - 1][col - 1], M[row][col - 1], M[row + 1][col - 1])
            M[-1][col] += min(M[-1][col - 1], M[-2][col - 1])

    # find minimum vertical energy seam. returns col indices in reverse row order (from bottom to top)
    def findVSeam(self):
        self.generateEMap()
        M = list(self.energyMap)
        # 0th row remains the same
        for row in range (1, self.row):
            M[row][0] += min(M[row - 1][0], M[row - 1][1])
            for col in range (1, self.col - 1):
                M[row][col] += min(M[row - 1][col - 1], M[row - 1][col], M[row - 1][col + 1])
            M[row][-1] += min(M[row - 1][-1], M[row - 1][-2])
        index_min = M[-1].index(min(M[-1]))
        vertical = []
        vertical.append(index_min)
        for row in range (self.row - 2, -1, -1):
            if index_min == 0:
                if M[row][index_min] > M[row][index_min + 1]:
                    index_min = index_min + 1
            elif index_min == self.col - 1:
                if M[row][index_min] > M[row][index_min - 1]:
                    index_min = index_min - 1
            else:
                if M[row][index_min] > M[row][index_min - 1]:
                    if M[row][index_min - 1] > M[row][index_min + 1]:
                        index_min = index_min + 1
                    else:
                        index_min = index_min - 1
                else:
                    if M[row][index_min] > M[row][index_min + 1]:
                        index_min = index_min + 1
            vertical.append(index_min)

        return vertical
    
    def transposeEMap(self):
        transposed = []
        self.generateEMap()
        for i in range (0, self.col):
            transposed.append([])
            for j in range (0, self.row):
                transposed[i].append(self.energyMap[j][i])

        return transposed


    # still need work... column extraction??
    def findHSeam(self):
        M = list(self.transposeEMap())
        # 0th row remains the same
        for col in range (1, self.col):
            M[0][col] += min(M[0][col - 1], M[1][col - 1])
            for row in range (1, self.row - 1):
                M[row][col] += min(M[row - 1][col - 1], M[row][col - 1], M[row + 1][col - 1])
            M[-1][col] += min(M[-1][col - 1], M[-2][col - 1])
        
        
  #      index_min = M[-1].index(min(M[-1]))
   #     vertical = []
    #    vertical.append(index_min)
     #   for row in range (self.row - 2, -1, -1):
      #      if index_min == 0:
       #         if M[row][index_min] > M[row][index_min + 1]:
        #            index_min = index_min + 1
         #   elif index_min == self.col - 1:
#if M[row][index_min] > M[row][index_min - 1]:
       #             index_min = index_min - 1
        #    else:
         #       if M[row][index_min] > M[row][index_min - 1]:
          #          if M[row][index_min - 1] > M[row][index_min + 1]:
           #             index_min = index_min + 1
            #        else:
             #           index_min = index_min - 1
              #  else:
               #     if M[row][index_min] > M[row][index_min + 1]:
                #        index_min = index_min + 1
           # vertical.append(index_min)

        for row in range (1, self.col):
            M[row][0] += min(M[row - 1][0], M[row - 1][1])
            for col in range (1, self.row - 1):
                M[row][col] += min(M[row - 1][col - 1], M[row - 1][col], M[row - 1][col + 1])
            M[row][-1] += min(M[row - 1][-1], M[row - 1][-2])
        index_min = M[-1].index(min(M[-1]))
        vertical = []
        vertical.append(index_min)
        for row in range (self.col - 2, -1, -1):
            if index_min == 0:
                if M[row][index_min] > M[row][index_min + 1]:
                    index_min = index_min + 1
            elif index_min == self.row - 1:
                if M[row][index_min] > M[row][index_min - 1]:
                    index_min = index_min - 1
            else:
                if M[row][index_min] > M[row][index_min - 1]:
                    if M[row][index_min - 1] > M[row][index_min + 1]:
                        index_min = index_min + 1
                    else:
                        index_min = index_min - 1
                else:
                    if M[row][index_min] > M[row][index_min + 1]:
                        index_min = index_min + 1
            vertical.append(index_min)

        return vertical

    # returns new image
    
    def removeVSeam(self):
        seam = self.findVSeam()
        new_data = np.
        for row in range (0, self.row):
            new_data.append([])
            deleted = seam.pop()
            for i in range (0, deleted):
                new_data[row].append(self.m_data[row][i])
            for i in range (deleted + 1, self.col):
                new_data[row].append(self.m_data[row][i])
            #self.m_data[row] = self.m_data[row][:(seam[-1 - row])].extend(self.m_data[row][(seam[-1 - row]) + 1:])
    
        return new_data

    
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

    def markAllSeams(self, newHeight, newWidth):
        numVertiSeams = self.col - newWidth
        numHoriSeams = self.row - newHeight
        
        for i in range (0, numVertiSeams):
            self.markVerticalSeam()

        for i in range (0, numHoriSeams):
            self.markHorizontalSeam()

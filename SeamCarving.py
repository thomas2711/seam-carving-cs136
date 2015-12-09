import matplotlib.image as mpli
import math
import numpy as np


class SeamCarver:
    # an RGB 2d array
    m_data = None
    row = 0 #y
    col = 0 #x
    energyMap = None
    abcd = None
    
    
    def __init__(self, imagePath):
        self.m_data = mpli.imread(imagePath)
        self.row = len(self.m_data)
        self.col = len(self.m_data[0])
        #generateEMap()
    
        #self.abcd = self.toGrayscale()
        #self.abcd = self.generateEnergyMap(self.toGrayscale())
        #self.abcd = self.generateEnergyMap()

    def toGrayscale(self):
        z = np.zeros((self.row, self.col, 3), dtype=np.uint8) #[[[0 for i in range(self.row)] for i in range(self.col)] for i in range(3)]
        for x in range (0, self.col): #x
            for y in range (0, self.row): #y
                g_rgb = 0.2989 * (float)(self.m_data[y][x][0]) + 0.5870 * (float)(self.m_data[y][x][1]) + 0.1140 * (float)(self.m_data[y][x][2])
                z[y][x][0] = g_rgb
                z[y][x][1] = g_rgb
                z[y][x][2] = g_rgb
        return z

    def generateEnergyMap(self):
        z = np.zeros((self.row, self.col, 3), dtype=np.uint8) #[[[0 for i in range(self.row)] for i in range(self.col)] for i in range(3)]
        for x in range (0, self.col): #x
            for y in range (0, self.row): #y
                pixel_energy = np.uint8(self.energy(x, y))
                z[y][x][0] = pixel_energy
                z[y][x][1] = pixel_energy
                z[y][x][2] = pixel_energy
        return z


    # returns energy of specified pixel
    def energy(self, x, y):
        return math.sqrt((self.rgb2gray(x - 1, y) - self.rgb2gray((x + 1) % self.col, y))**2 + (self.rgb2gray(x, y - 1) - self.rgb2gray(x, (y + 1) % self.row))**2)
    
    def generateEMap(self):
        self.energyMap = []
        for i in range (0, self.row):
            self.energyMap.append([])
            for j in range (0, self.col):
                self.energyMap[i].append(self.energy(j, i))

    # Matlab formula
    def rgb2gray(self, x, y):
        return 0.2989 * (int)(self.m_data[y][x][0]) + 0.5870 * (int)(self.m_data[y][x][1]) + 0.1140 * (int)(self.m_data[y][x][2])
    
    
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
        new_data = np.ndarray((self.row, self.col - 1, 3), np.uint8)
        for row in range (0, self.row):
            deleted = seam.pop()
            for i in range (0, deleted):
                new_data[row][i][0] = self.m_data[row][i][0]
                new_data[row][i][1] = self.m_data[row][i][1]
                new_data[row][i][2] = self.m_data[row][i][2]
            for i in range (deleted + 1, self.col):
                new_data[row][i - 1][0] = self.m_data[row][i][0]
                new_data[row][i - 1][1] = self.m_data[row][i][1]
                new_data[row][i - 1][2] = self.m_data[row][i][2]

        return new_data
        
    def removeHSeam(self):
        seam = self.findHSeam()
        new_data = np.ndarray((self.row - 1, self.col, 3), np.uint8)
        for col in range (0, self.col):
            deleted = seam.pop()
            for i in range (0, deleted):
                new_data[i][col][0] = self.m_data[i][col][0]
                new_data[i][col][1] = self.m_data[i][col][1]
                new_data[i][col][2] = self.m_data[i][col][2]
            for i in range (deleted + 1, self.row):
                new_data[i - 1][col][0] = self.m_data[i][col][0]
                new_data[i - 1][col][1] = self.m_data[i][col][1]
                new_data[i - 1][col][2] = self.m_data[i][col][2]
    
        return new_data

    def addVSeam(self):
        seam = self.findVSeam()
        new_data = np.ndarray((self.row, self.col + 1, 3), np.uint8)

        
        #new_data = np.ndarray((self.row, self.col + 1, 3), np.uint8)
        for row in range (0, self.row):
            added = seam.pop()
            for i in range (0, added + 1):
                new_data[row][i][0] = self.m_data[row][i][0]
                new_data[row][i][1] = self.m_data[row][i][1]
                new_data[row][i][2] = self.m_data[row][i][2]
            
            for i in range (added, self.col):
                new_data[row][i + 1][0] = self.m_data[row][i][0]
                new_data[row][i + 1][1] = self.m_data[row][i][1]
                new_data[row][i + 1][2] = self.m_data[row][i][2]

        return new_data

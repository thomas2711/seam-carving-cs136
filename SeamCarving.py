import numpy
from PIL import Image
from sys import maxsize
from math import sqrt

class SeamCarver:
    data = None
    greyscale_data = None
    y = 0 #rows
    x = 0 #cols
    energy_map = None
    
    def __init__(self, path):
        self.data = numpy.array(Image.open(path))
        self.y = len(self.data)
        self.x = len(self.data[0])
    
    def save_image_as(self, filename = "output.png"):
        Image.fromarray(self.data).save(filename)

    # uses Matlab greyscale formula
    def to_greyscale(self):
        z = numpy.zeros((self.y, self.x), dtype=numpy.uint8)
        for x in range (0, self.x):
            for y in range(0, self.y):
                greyscale_rgb_val = 0.2989 * (float)(self.data[y][x][0]) + 0.5870 * (float)(self.data[y][x][1]) + 0.1140 * (float)(self.data[y][x][2])
                z[y][x] = greyscale_rgb_val
        self.greyscale_data = z
    
    # the lighter a pixel is, the higher its energy is
    def render_energy_map(self):
        if self.energy_map == None:
            self.generate_energy_map()
        z = numpy.zeros((self.y, self.x, 3), dtype=numpy.uint8)
        for x in range(0, self.x):
            for y in range (0, self.y):
                pixel_energy = numpy.uint8(self.energy_map[y][x])
                z[y][x][0] = pixel_energy
                z[y][x][0] = pixel_energy
                z[y][x][0] = pixel_energy
        return z

    def generate_energy_map(self):
        self.energy_map = []
        for i in range(0, self.y):
            self.energy_map.append([])
            for j in range(0, self.x):
                self.energy_map[i].append(self.energy(j, i))
        #self.adjust_energy()

    # adjust energy array so that pixels between specified area are removed
    def adjust_energy(self):
        for i in range(self.x1, self.x2):
            for z in range(self.y1, self.y2):
                self.energy_map[z][i] = -maxsize - 1

    def remove_pixels(self, x1, y1, x2, y2):
        self.x1 = x1
        self.x2 = x2
        self.y1 = y1
        self.y2 = y2

    def energy(self, x, y):
        return sqrt((self.greyscale_val(x - 1, y) - self.greyscale_val((x + 1) % self.x, y))**2 + (self.greyscale_val(x, y - 1) - self.greyscale_val(x, (y + 1) % self.y))**2)

    def greyscale_val(self, x, y):
        return int(self.greyscale_data[y][x])

    def mark_vert_seam(self):
        seam = self.find_seam(vert = True)
        for i in range(0, self.y):
            self.data[i][seam[i]][0] = 255
            self.data[i][seam[i]][1] = 0
            self.data[i][seam[i]][2] = 0

    def mark_h_seam(self):
        seam = self.find_seam(vert = False)
        for i in range(0, self.x):
            self.data[i][seam[i]][0] = 255
            self.data[i][seam[i]][1] = 0
            self.data[i][seam[i]][2] = 0

    def transpose_emap(self):
        transposed = []
        for i in range (0, self.x):
            transposed.append([])
            for j in range (0, self.y):
                transposed[i].append(self.energy_map[j][i])
        return transposed

    def find_seam(self, vert = True):
        if not vert: #horizontal
            tem = list(self.transpose_emap())
        else:
            tem = list(self.energy_map)
        # start at second row
        for row in range(1, len(tem)):
            # first pixel, special case
            tem[row][0] += min(tem[row-1][0], tem[row - 1][1])
            for col in range(1, self.x - 1):
                tem[row][col] += min(tem[row - 1][col - 1], tem[row - 1][col], tem[row][col - 1])
            # last pixel, special case
            tem[row][-1] += min(tem[row - 1][col - 1], tem[row - 1][-2])

        index_min = tem[-1].index(min(tem[-1]))

        vertical_seams = []
        vertical_seams.append(index_min)
        for row in range(len(tem) - 2, -1, -1):
            if index_min == 0:
                if tem[row][index_min] > tem[row][index_min+1]:
                    index_min = index_min + 1
            elif index_min == len(tem[0]) - 1:
                if tem[row][index_min] > tem[row][index_min - 1]:
                    index_min = index_min - 1
            else:
                if tem[row][index_min] > tem[row][index_min - 1]:
                    if tem[row][index_min - 1] > tem[row][index_min + 1]:
                        index_min = index_min + 1
                    else:
                        index_min = index_min - 1
                else:
                    if tem[row][index_min] > tem[row][index_min + 1]:
                        index_min = index_min + 1
            vertical_seams.append(index_min)
        return vertical_seams

    def remove_v_seam(self):
        seam = self.find_seam(vert = True)
        test = seam.copy()
        new_data = numpy.ndarray((self.y, self.x - 1, 3), numpy.uint8)
        g_new_data = numpy.ndarray((self.y, self.x - 1), numpy.uint8)
        #e_new_data = [[0 for x in range(self.x-1)] for y in range(self.y)] 
        for row in range (0, self.y):
            deleted = seam.pop()
            if deleted == self.x: #end col
                for i in range(0, self.x-1):
                    new_data[row][i][0] = self.data[row][i][0]
                    new_data[row][i][1] = self.data[row][i][1]
                    new_data[row][i][2] = self.data[row][i][2]
                    #greyscale
                    g_new_data[row][i] = self.greyscale_data[row][i]
                    #energy_map
                    #e_new_data[row][i] = self.energy_map[row][i]
            else:
                for i in range(0, deleted):
                    new_data[row][i][0] = self.data[row][i][0]
                    new_data[row][i][1] = self.data[row][i][1]
                    new_data[row][i][2] = self.data[row][i][2]
                    #greyscale
                    g_new_data[row][i] = self.greyscale_data[row][i]
                    #energy_map
                    #e_new_data[row][i] = self.energy_map[row][i]
                for i in range(deleted + 1, self.x):
                    new_data[row][i - 1][0] = self.data[row][i][0]
                    new_data[row][i - 1][1] = self.data[row][i][1]
                    new_data[row][i - 1][2] = self.data[row][i][2]
                    #greyscale
                    g_new_data[row][i - 1] = self.greyscale_data[row][i]
                    #energy_map
                    #e_new_data[row][i - 1] = self.energy_map[row][i]
        self.data = new_data.copy()
        self.greyscale_data = g_new_data.copy()
        self.x -= 1


        '''
        for row in range(0, self.y):
            d = test.pop()
            if d < self.x:
                e_new_data[row][d] = self.energy(d, row)
            e_new_data[row][d-1] = self.energy(d-1, row)
        self.energy_map = e_new_data.copy()
        return self.energy_map
    '''


sc = SeamCarver("example_8.jpg")
sc.to_greyscale()
import time
start_time = time.time()
sc.generate_energy_map()
#print(sc.x)
for x in range(0, 5):
    #print(x)
    sc.remove_v_seam()
    sc.generate_energy_map()
sc.save_image_as()
print("--- %s seconds ---" % (time.time() - start_time))


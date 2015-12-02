
class SeamCarver:
    # an RGB 2d array
    m_data = None
    
    def __init__(self, imagePath):
        # TODO: imsave method
        matplotlib.image.imsave(imagePath, self.m_data)

    # returns energy of specified pixel
    def energy(x, y):
        # TODO

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

from SeamCarving import *

def resize(imagePath, newHeight, newWidth, newImagePath = "resized.png"):

    s = SeamCarver(imagePath)
    removeHSeams = True
    removeVSeams = True
    if newHeight > s.row: removeHSeams = False
    if newWidth > s.col: removeVSeams = False
        
    for i in range (0, abs(newHeight - s.row)):
        if removeHSeams: s.removeHSeam()
        else: s.addHSeam()
        mpli.imsave(newImagePath, s.m_data)

    for i in range (0, abs(newWidth - s.col)):
        if removeVSeams: s.removeVSeam()
        else: s.addVSeam()
        mpli.imsave(newImagePath, s.m_data)


if __name__ == '__main__':
    
    newHeight = 300
    newWidth = 400
    imagePath = "images/example_7.jpg"
    newImagePath = "results/result_2.png"
    resize(imagePath, newHeight, newWidth, newImagePath)


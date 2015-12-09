from SeamCarving import *

print("this is a test!")

s = SeamCarver("images/example_2.jpg")
#s.adjustEnergy(17, 135, 32, 159)
s.excludePixels(17, 135, 32, 159, False)
for i in range(0, 20):
    s.removeVSeam()
s.saveImageAs()

#image = mpli.imread("images/example_1.jpg")
#
#for x in image:
#    for i in x:
#        # i = each pixel with rgb values
#        i[0] = 0 # r
#        i[1] = 0 # g
#        i[2] = 100 # b
#
#
#mpli.imsave("test.jpg", image)
#for x in image:
#    for i in x:
#        # i = each pixel with rgb values
#        i[0] = 0 # r
#        i[1] = 0 # g
#        i[2] = 100 # b
#
#mpli.imsave("test.jpg", image)

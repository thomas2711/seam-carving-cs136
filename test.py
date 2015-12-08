from SeamCarving import *

print("this is a test!")

s = SeamCarver("images/example_1.jpg")
mpli.imsave("test.jpg", s.m_data)

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

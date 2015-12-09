from SeamCarving import *

s = SeamCarver("images/example_5.jpg")

for i in range (0, 10):
    s.addHSeam()
    mpli.imsave("removed.jpg", s.m_data)
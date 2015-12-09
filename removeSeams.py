from SeamCarving import *

s = SeamCarver("images/example_7.jpg")

for i in range (0, 200):
    s.removeVSeam()
    mpli.imsave("removed.jpg", s.m_data)
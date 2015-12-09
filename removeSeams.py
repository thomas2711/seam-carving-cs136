from SeamCarving import *

s = SeamCarver("images/example_6.jpg")
#s.markHorizontalSeam()
#mpli.imsave("hseam.jpg", s.m_data)
for i in range (0, 50):
    mpli.imsave("removed.jpg", s.addVSeam())
    s = SeamCarver("removed.jpg")

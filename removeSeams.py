from SeamCarving import *

s = SeamCarver("images/example_4.jpg")

for i in range (0, 100):
    mpli.imsave("removed.jpg", s.removeVSeam())
    s = SeamCarver("removed.jpg")

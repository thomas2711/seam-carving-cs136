import matplotlib.image as mpli

print("this is a test!")

image = mpli.imread("images/example_1.jpg")

for x in image:
    for i in x:
        # i = each pixel with rgb values
        i[0] = 0 # r
        i[1] = 0 # g
        i[2] = 100 # b


mpli.imsave("test.jpg", image)

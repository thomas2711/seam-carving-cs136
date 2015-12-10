Williams College, CS136, Prof. Morgan McGuire
Final Project
Thomas Edward Ragucci, ter1@williams.edu
Zhiqi Li, zl2@williams.edu
Mentor: Jamie Lesser, jrl4@williams.edu

This program is an Python3 implementation to reproduce the Seam Carving algorithm [Avidan and Shamir].

It uses the following libraries:
numpy
matplotlib
math

It includes the following files: 
SeamCarving.py


Instructions:
The program has two features: (1) resize the image to a smaller size; (2) remove object in specified box of pixels in the image.
(1) the method -- resize(imagePath, newHeight, newWidth, newImagePath) --  saves the resized image to the specified location
(2) the method -- removeObject(imagePath, x1, y1, x2, y2, newImagePath) -- removes the content contained by (x1, y1), (x2, y1), (x2, y2), (x1, y2) and saves the new image to the specified location


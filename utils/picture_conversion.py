import cv2 
from PIL import Image

def read_image():
    # read the image file
    img = cv2.imread('drawn_picture.png', 2)
    img = cv2.resize(img, (40, 40))

    f = open("../ev3/image_array.txt", "w+")
    # loop over all pixels and convert to True or False/1 or 0/0 or 255
    for c1, pixel_line in enumerate(img):
        for c2, pixel in enumerate(pixel_line):
            # is pixel darker than threshold?
            if int(pixel) < 140:
                img[c1][c2] = 0 # for picture
                f.write(" 1 ") # for array
            else:
                img[c1][c2] = 255 # for picture
                f.write(" 0 ")  # for array
        f.write("\n")


    f.close()
    return img

img = read_image()

image = Image.fromarray(img)
image.save("picture_from_array.png")

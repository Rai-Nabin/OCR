import numpy as np
import cv2 as cv
import os
import shutil

def crop_image(idx, image, coordinates):

    points = np.array([coordinates], dtype=np.int32)

    # Returns lowest (x-axis, y-axis), maximumum(width and height) of the rectangle
    rectangle = cv.boundingRect(points)

    cropped_image = image[rectangle[1]: rectangle[1] +
                          rectangle[3], rectangle[0]: rectangle[0]+rectangle[2]]
    cv.imwrite(f'images/cropped_image/crop_{idx}.jpg', cropped_image)
    # return cropped_image

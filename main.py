import os
import shutil
import sys

import cv2 as cv
import numpy as np

from src.crop_image import crop_image
from src.detect_text import (detect_text_cooridinates,
                             draw_bounding_box_and_save)
from src.extract_text import extract_text
from src.preprocess import show_image
from src.save_output import save_to_json
from src.plot_text import plot_text


def main():
    INPUT_IMAGE_PATH = sys.argv[1]

    FILE_NAME = INPUT_IMAGE_PATH.split('/')[-1].split('.')[0]
    
    image = cv.imread(INPUT_IMAGE_PATH)
    # show_image(image)
    original_image = image.copy()

    sorted_bounding_boxes = detect_text_cooridinates(INPUT_IMAGE_PATH)

    draw_bounding_box_and_save(image, sorted_bounding_boxes, FILE_NAME)
    
    folder_path = f'images/cropped_image'

    if not os.path.isdir(folder_path):
        os.makedirs(folder_path)
    else:
        shutil.rmtree(folder_path)
        os.makedirs(folder_path)

    text = {}

    for idx, coordinates in enumerate(sorted_bounding_boxes):
        crop_image(idx, original_image, coordinates)
        cropped_image_path = f'images/cropped_image/crop_{idx}.jpg'
        extracted_text = extract_text(cropped_image_path)
        text[idx+1] = extracted_text

    plot_text(image, sorted_bounding_boxes, text, FILE_NAME)

    save_to_json(text, FILE_NAME)


if __name__ == "__main__":
    main()

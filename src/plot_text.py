
import cv2 as cv
import numpy as np
from PIL import Image, ImageDraw, ImageFont

from src.preprocess import show_image


def draw_empty_canvas(image):
    image_height = image.shape[0]
    image_width = image.shape[1]

    image_canvas = np.zeros((image_height, image_width, 3), np.uint8)
    image_canvas.fill(255)

    return image_canvas
    


def plot_text(image, sorted_bounding_boxes, text, FILE_NAME):

    canvas = draw_empty_canvas(image)

    font_path = f'./fonts/simfang.ttf'
    font = ImageFont.truetype(font_path, 70)

    pillow_image = Image.fromarray(canvas)
    draw_image = ImageDraw.Draw(pillow_image)

    for idx, coordinates in enumerate(sorted_bounding_boxes):
        x = coordinates[:][0][0]
        y = coordinates[:][0][1]

        txt = text.get(idx+1)

        draw_image.text((int(x), int(y)), txt, font=font, fill=(0, 0, 0))

    image = np.array(pillow_image)

    # show_image(image)
    cv.imwrite(f"./output/{FILE_NAME}_canvas.jpg", image)

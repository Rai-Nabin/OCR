import cv2 as cv


def resize_image(image):

    image_height, image_width = image.shape[:2]

    if image_width and image_height > 1000:
        width = 1000
        height = 800
        dim = (width, height)
        return cv.resize(image, dim, interpolation=cv.INTER_AREA)
    else:
        return image


def show_image(image, window_name="Sample Image"):

    resized_image = resize_image(image)

    cv.imshow(window_name, resized_image)
    cv.waitKey(0)
    cv.destroyAllWindows()

import numpy as np
from PIL import Image

def resize_image(image, scale_percent):
    """
    Resize the image by a percentage of original size.
    """
    if scale_percent <= 0 or scale_percent > 100:
        raise ValueError("Scale percent must be between 1 and 100.")

    original = Image.fromarray(np.uint8(image))
    new_width = int(original.width * scale_percent / 100)
    new_height = int(original.height * scale_percent / 100)

    resized = original.resize((new_width, new_height), Image.LANCZOS)
    return np.array(resized)


def invert(image):
    return 255 - image

def grayscale(image):
    if len(image.shape) == 3:
        return np.mean(image, axis=2).astype(np.uint8)
    return image

def adjust_brightness(image, value):
    return np.clip(image + value, 0, 255)

def flip(image, direction="horizontal"):
    if direction == "horizontal":
        return np.fliplr(image)
    elif direction == "vertical":
        return np.flipud(image)

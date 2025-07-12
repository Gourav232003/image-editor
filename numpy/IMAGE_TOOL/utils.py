import numpy as np
from PIL import Image
import matplotlib.pyplot as plt

def load_image(path):
    image = Image.open(path)
    return np.array(image)

def save_image(path, array):
    img = Image.fromarray(np.uint8(array))
    img.save(path)

def show_image(array):
    plt.imshow(array, cmap='gray' if len(array.shape) == 2 else None)
    plt.axis('off')
    plt.show()

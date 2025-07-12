import numpy as np
from scipy.signal import convolve2d
from image_operations import grayscale

def apply_blur(image):
    kernel = np.ones((3, 3)) / 9
    if len(image.shape) == 3:
        return np.stack([convolve2d(image[:, :, i], kernel, mode='same', boundary='symm') for i in range(3)], axis=2)
    else:
        return convolve2d(image, kernel, mode='same', boundary='symm')

def apply_edge_detection(image):
    image = grayscale(image)
    sobel_x = np.array([[1, 0, -1],
                        [2, 0, -2],
                        [1, 0, -1]])
    sobel_y = np.array([[1, 2, 1],
                        [0, 0, 0],
                        [-1, -2, -1]])

    gx = convolve2d(image, sobel_x, mode='same', boundary='symm')
    gy = convolve2d(image, sobel_y, mode='same', boundary='symm')
    edges = np.sqrt(gx**2 + gy**2)
    return np.clip(edges, 0, 255)

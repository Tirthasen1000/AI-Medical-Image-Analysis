import cv2
import numpy as np

IMG_SIZE = 64

def preprocess_image(image_path):
    """
    Load and preprocess a single image
    """

    # Read image
    image = cv2.imread(image_path)

    # Resize image
    image = cv2.resize(image, (IMG_SIZE, IMG_SIZE))

    # Normalize (0–255 → 0–1)
    image = image / 255.0

    return image


def preprocess_batch(image_paths):
    """
    Process multiple images
    """
    data = []

    for path in image_paths:
        img = preprocess_image(path)
        data.append(img)

    return np.array(data)
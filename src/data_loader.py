import numpy as np
import cv2
import os

IMG_SIZE = 64

def load_data():
    data = []
    labels = []

    for category in ["normal", "tumor"]:
        path = os.path.join("data", category)
        label = 0 if category == "normal" else 1

        for img in os.listdir(path):
            img_path = os.path.join(path, img)
            image = cv2.imread(img_path)
            image = cv2.resize(image, (IMG_SIZE, IMG_SIZE))

            data.append(image)
            labels.append(label)

    data = np.array(data) / 255.0
    labels = np.array(labels)

    split = int(0.8 * len(data))

    return data[:split], data[split:], labels[:split], labels[split:]
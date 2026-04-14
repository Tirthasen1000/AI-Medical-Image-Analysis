import cv2
import numpy as np

IMG_SIZE = 64

def predict_image(model, image_path):
    """
    Predict tumor from a single image
    """

    # 🔹 Load image
    image = cv2.imread(image_path)

    if image is None:
        print("❌ Error: Image not found!")
        return

    # 🔹 Resize
    image = cv2.resize(image, (IMG_SIZE, IMG_SIZE))

    # 🔹 Normalize
    image = image / 255.0

    # 🔹 Reshape for model
    image = np.reshape(image, (1, IMG_SIZE, IMG_SIZE, 3))

    # 🔹 Predict
    prediction = model.predict(image)[0][0]

    # 🔹 Output with confidence
    if prediction > 0.5:
        print(f"🧠 Tumor Detected (Confidence: {prediction:.2f})")
    else:
        print(f"✅ Normal Brain (Confidence: {1 - prediction:.2f})")
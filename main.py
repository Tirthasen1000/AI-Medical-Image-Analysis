from src.data_loader import load_data
from src.model import build_model
from src.train import train_model
from src.evaluate import evaluate_model
from src.visualize import show_sample_images, show_predictions, plot_accuracy
from src.predict import predict_image

import os

def main():
    print("🚀 Starting Medical Image AI Project...")

    # 🔹 Load data
    X_train, X_test, y_train, y_test = load_data()
    print("✅ Data Loaded")

    # 🔹 Show sample images
    show_sample_images(X_train, y_train)

    # 🔹 Build model
    model = build_model()
    print("✅ Model Built")

    # 🔹 Train model (returns history)
    model, history = train_model(model, X_train, y_train)
    print("✅ Model Trained")

    # 🔥 CALL GRAPH FUNCTION HERE
    plot_accuracy(history)

    # 🔹 Predict on test data
    predictions = model.predict(X_test)
    print("✅ Prediction Done")

    # 🔹 Evaluate model
    evaluate_model(model, X_test, y_test)

    # 🔹 Show predictions visually
    show_predictions(X_test, y_test, predictions)

    # 🔹 Single image prediction (auto pick)
    sample_image = os.listdir("data/tumor")[0]
    predict_image(model, f"data/tumor/Te-aug-me_21.jpg")

    print("🎉 Project Completed Successfully!")

if __name__ == "__main__":
    main()
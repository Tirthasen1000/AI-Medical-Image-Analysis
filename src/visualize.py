import matplotlib.pyplot as plt

def show_sample_images(X, y):
    """
    Display sample images with labels
    """

    plt.figure(figsize=(8, 6))

    for i in range(6):
        plt.subplot(2, 3, i + 1)
        plt.imshow(X[i])
        plt.title("Tumor" if y[i] == 1 else "Normal")
        plt.axis("off")

    plt.suptitle("Sample Medical Images")
    plt.show()


def show_predictions(X_test, y_test, predictions):
    """
    Display predictions vs actual labels
    """

    plt.figure(figsize=(8, 6))

    for i in range(6):
        plt.subplot(2, 3, i + 1)
        plt.imshow(X_test[i])

        pred_label = "Tumor" if predictions[i] > 0.5 else "Normal"
        true_label = "Tumor" if y_test[i] == 1 else "Normal"

        plt.title(f"P: {pred_label}\nT: {true_label}")
        plt.axis("off")

    plt.suptitle("Predictions vs Actual")
    plt.show()


def plot_accuracy(history):
    """
    Plot training accuracy graph
    """

    plt.figure()

    plt.plot(history.history['accuracy'], label='Train Accuracy')
    plt.plot(history.history['val_accuracy'], label='Validation Accuracy')

    plt.title("Model Accuracy")
    plt.xlabel("Epochs")
    plt.ylabel("Accuracy")

    plt.legend()
    plt.grid()

    plt.show()
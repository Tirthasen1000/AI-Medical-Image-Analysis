def train_model(model, X_train, y_train):
    history = model.fit(
        X_train,
        y_train,
        epochs=10,
        batch_size=32,
        validation_split=0.2
    )

    model.save("models/model.keras")

    print("💾 Model Saved Successfully!")

    return model, history
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPool2D, Dense, Flatten, Dropout


def build_cnn_model(input_shape=(128, 128, 3)):
    """
    Build the CNN architecture used for binary image classification.

    The model receives an image and predicts whether it is real or AI generated.
    """
    model = Sequential(
        [
            Conv2D(32, (5, 5), activation="relu", input_shape=input_shape),
            Conv2D(32, (5, 5), activation="relu"),
            MaxPool2D((2, 2)),
            Dropout(0.25),
            Flatten(),
            Dense(256, activation="relu"),
            Dropout(0.5),
            Dense(2, activation="softmax"),
        ]
    )

    model.compile(
        optimizer="adam",
        loss="categorical_crossentropy",
        metrics=["accuracy"],
    )

    return model
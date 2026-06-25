from pathlib import Path

import numpy as np
from tensorflow.keras.models import load_model

from src.model import build_cnn_model
from src.preprocessing import prepare_image


CLASS_NAMES = {
    0: "Fake Image",
    1: "Real Image",
}


def load_prediction_model(model_path):
    """
    Load a trained model from disk.

    The function first tries to load a full saved Keras model.
    If that fails, it falls back to building the model architecture and loading weights.
    """
    model_path = Path(model_path)

    if not model_path.exists():
        raise FileNotFoundError(f"Model file was not found: {model_path}")

    try:
        return load_model(model_path)
    except Exception:
        model = build_cnn_model()
        model.load_weights(model_path)
        return model


class ImageClassifier:
    """
    Wrapper class for image classification.
    """

    def __init__(self, model_path):
        self.model = load_prediction_model(model_path)

    def predict(self, image_path):
        """
        Predict whether an image is real or AI generated.
        """
        image = prepare_image(image_path)
        prediction = self.model.predict(image, verbose=0)

        predicted_class = int(np.argmax(prediction, axis=1)[0])
        confidence = float(np.max(prediction))

        return {
            "class_index": predicted_class,
            "label": CLASS_NAMES.get(predicted_class, "Unknown"),
            "confidence": confidence,
        }
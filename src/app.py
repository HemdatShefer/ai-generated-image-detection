from pathlib import Path

from flask import Flask, jsonify, request
from werkzeug.utils import secure_filename

from src.predict import ImageClassifier


BASE_DIR = Path(__file__).resolve().parent.parent
MODEL_PATH = BASE_DIR / "models" / "cnn_pilot_saving_model.h5"
UPLOADS_DIR = BASE_DIR / "uploads"

ALLOWED_EXTENSIONS = {"jpg", "jpeg", "png"}

app = Flask(
    __name__,
    static_folder=str(BASE_DIR / "web"),
    static_url_path="",
)

_classifier = None


def is_allowed_file(filename):
    """
    Check whether the uploaded file has an allowed image extension.
    """
    return "." in filename and filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS


def get_classifier():
    """
    Lazy load the classifier only when a prediction request is received.
    """
    global _classifier

    if _classifier is None:
        _classifier = ImageClassifier(MODEL_PATH)

    return _classifier


@app.route("/", methods=["GET"])
def home():
    """
    Serve the frontend index file if it exists.
    """
    index_path = BASE_DIR / "web" / "index.html"

    if index_path.exists():
        return app.send_static_file("index.html")

    return jsonify(
        {
            "message": "RealityCheck API is running",
            "predict_endpoint": "/predict",
        }
    )


@app.route("/predict", methods=["POST"])
def predict_image():
    """
    Receive an uploaded image and return the model prediction.
    """
    if "file" not in request.files:
        return jsonify({"error": "No file was uploaded"}), 400

    uploaded_file = request.files["file"]

    if uploaded_file.filename == "":
        return jsonify({"error": "No file was selected"}), 400

    if not is_allowed_file(uploaded_file.filename):
        return jsonify({"error": "Only jpg, jpeg, and png files are supported"}), 400

    UPLOADS_DIR.mkdir(exist_ok=True)

    filename = secure_filename(uploaded_file.filename)
    image_path = UPLOADS_DIR / filename

    try:
        uploaded_file.save(image_path)

        classifier = get_classifier()
        result = classifier.predict(image_path)

        return jsonify(result)

    except FileNotFoundError as error:
        return jsonify({"error": str(error)}), 500

    finally:
        if image_path.exists():
            image_path.unlink()


if __name__ == "__main__":
    app.run(debug=True)
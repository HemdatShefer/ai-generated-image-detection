import os
import tempfile
from pathlib import Path

import numpy as np
from PIL import Image, ImageChops, ImageEnhance


IMAGE_SIZE = (128, 128)


def convert_to_ela_image(image_path, quality=90):
    """
    Convert an image into Error Level Analysis format.

    ELA highlights compression differences in the image and can help expose
    visual artifacts that may be useful for classification.
    """
    image_path = Path(image_path)
    temp_file = None

    try:
        original = Image.open(image_path).convert("RGB")

        with tempfile.NamedTemporaryFile(suffix=".jpg", delete=False) as temp:
            temp_file = temp.name

        original.save(temp_file, "JPEG", quality=quality)
        saved = Image.open(temp_file).convert("RGB")

        diff = ImageChops.difference(original, saved)
        extrema = diff.getextrema()
        max_diff = max(channel[1] for channel in extrema)

        if max_diff == 0:
            max_diff = 1

        scale = 255.0 / max_diff
        ela_image = ImageEnhance.Brightness(diff).enhance(scale)

        return ela_image

    finally:
        if temp_file and os.path.exists(temp_file):
            os.remove(temp_file)


def prepare_image(image_path, image_size=IMAGE_SIZE):
    """
    Prepare an image for model prediction.

    The function converts the image to ELA format, resizes it, normalizes pixel
    values, and reshapes it to match the CNN input shape.
    """
    ela_image = convert_to_ela_image(image_path).resize(image_size)
    image_array = np.asarray(ela_image).astype("float32") / 255.0

    return image_array.reshape(1, image_size[0], image_size[1], 3)
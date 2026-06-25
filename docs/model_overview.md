# Model Overview

The project uses a CNN based binary image classifier.

The model receives an image after preprocessing and predicts one of two classes:

- Fake Image
- Real Image

## Preprocessing

Before prediction, the image is converted using Error Level Analysis.
The image is resized to 128 by 128 pixels, normalized, and reshaped to match the CNN input shape.

## Architecture

The model architecture includes:

- Two convolution layers
- Max pooling
- Dropout
- Dense layer
- Softmax output layer with two classes

## Input

Image size: 128 x 128 x 3

## Output

The model returns:

- Predicted class
- Confidence score

# RealityCheck, AI Generated Image Detection

RealityCheck is an academic machine learning project for classifying images as real or AI generated.

The project explores CNN based image classification, image preprocessing using Error Level Analysis, and integration of a trained model into a simple application flow.

## Overview

AI generated images are becoming increasingly realistic, making it harder to distinguish between real and synthetic visual content.

This project focuses on the binary classification task of identifying whether an input image is real or AI generated.

## Project Goals

The main goals of this project are:

- Preprocess input images for model prediction
- Use Error Level Analysis as part of the image preparation process
- Classify images using a CNN based model
- Connect the model prediction flow to a simple user facing application
- Organize the project code and documentation for future improvement

## Main Components

- Image preprocessing using Error Level Analysis
- CNN based image classification
- Model prediction flow
- Basic web interface for image upload and classification
- Server side integration experiments
- Project documentation and research summary

## Technologies

- Python
- TensorFlow
- Keras
- NumPy
- Pillow
- Matplotlib
- Scikit learn
- Flask
- HTML
- CSS
- JavaScript

## Repository Structure

```text
src/
  Python source code for preprocessing, model definition, prediction, and application logic

web/
  Frontend files for the user interface

legacy/
  Older experimental code kept for documentation and refactoring

docs/
  Project documentation and summaries
```

## Setup Instructions

Create and activate a virtual environment.

```cmd
python -m venv .venv
.venv\Scripts\activate
```

Install the required dependencies.

```cmd
pip install -r requirements.txt
```

## Model File

The trained model file is not included in this repository.

To run predictions locally, place the trained model file inside a local `models` directory.

Expected path:

```text
models/cnn_pilot_saving_model.h5
```

The `models` directory is ignored by Git because trained model files can be large and are not part of the source code.

## Running the Application

Run the Flask application from the project root.

```cmd
python -m src.app
```

Then open the local server address in the browser.

```text
http://127.0.0.1:5000
```

## Current Environment Note

If the application does not start because of a NumPy compatibility issue, recreate the virtual environment and install compatible dependency versions.

A common fix is to use a NumPy version below 2.

```cmd
pip install "numpy<2"
```

## Project Status

This project was originally developed as an academic group project.

The repository is currently being reorganized to clearly separate authored code, experimental code, documentation, and external reference material.

## Baseline Reference

The project was inspired by an external baseline implementation for real and AI generated image classification.

The original baseline code is not included as authored source code in this repository.

My work focused on understanding the baseline approach, experimenting with preprocessing and model usage, organizing the project structure, and integrating the model into an application flow.

## Future Improvements

- Refactor the model training pipeline
- Add clear dataset loading instructions
- Add evaluation metrics and visual results
- Improve the web application integration
- Add reproducible setup instructions
- Add examples of model predictions
- Add clearer separation between training code and inference code

## Notes

Large datasets, trained model files, and external reference code are not included in this repository.

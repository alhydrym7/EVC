# image_processing_app

https://github.com/alhydrym7/EVC_with_Open-cv/assets/50909741/15fa5a78-48ab-4b7c-bc52-7f76281f10ea

# Python Image Processing Application
  This is a Python application that allows you to perform various image processing operations on images. It provides a user-friendly interface to upload images, capture images     from a camera, and apply different image filters.

# Prerequisites
  Before running the application, ensure that you have the following dependencies installed:

  1. Python (version 3.x)
  2. OpenCV (cv2) library
  3. NumPy library
  4. tkinter library
  5. PIL (Python Imaging Library) library
  # You can install the required libraries using pip:
    pip install opencv-python numpy pillow 


# Getting Started
  # To run the application, follow these steps:

    1. Save the Python code provided in a file (e.g., image_processing_app.py).
    2. Open a terminal or command prompt and navigate to the directory where the file is saved.
    3. Run the Python script using the following command: [ python image_processing_app.py ]
    4. The application window will appear, allowing you to perform various image processing operations.

# Features
  # Selecting an Image:
    1. To select an image, click the "Select Image" button. A file dialog will open, allowing you to choose an image file (in JPEG, JPG, or PNG format) from your local system.
    2. Once an image is selected, it will be displayed in the application window.
  # Capturing Images from Camera:
    1. To capture an image from a camera, click the "Camera" button.
    2. The application will access your default camera and display the live camera feed in a separate window.
    3. Press the "S" key on your keyboard to capture an image. The captured image will be saved as "imageX.jpg" (where X is a number) in the current directory.
    4. The captured image will be displayed in the application window.

# Image Processing Filters
  The application provides the following image processing filters that can be applied to the selected or captured image:

  1. Rotate Horizontally: Rotates the image 90 degrees counter-clockwise.
  2. Flip: Flips the image horizontally.
  3. Grayscale: Converts the image to grayscale.
  4. Gaussian Blur: Applies Gaussian blur to the image.
  5. Edge Detection: Performs edge detection on the image.
  6. Smoothing: Applies a median blur to the image.
    To apply a filter, click on the respective button after selecting or capturing an image. The processed image will be displayed in the application window.

# Acknowledgments
    This application utilizes the capabilities of OpenCV, tkinter, and PIL libraries to provide an interactive image processing experience.



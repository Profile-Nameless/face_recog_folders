# Face Recognition Script

This Python script uses the OpenCV library to perform face detection in a collection of images stored in various folders. The script utilizes the Haar Cascade classifier for face detection and draws rectangles around the detected faces. Additionally, it counts and displays the number of faces detected in each image.

## Prerequisites

Make sure you have the required dependencies installed before running the script:

- OpenCV
  ```bash
  pip install opencv-python
Usage
Clone the repository or download the script.

bash
Copy code
git clone https://github.com/your-username/face-recognition-script.git
cd face-recognition-script
Place your images in folders within the specified root directory.

Run the script:

bash
Copy code
python face_recognition_script.py
View the output images with face detection results in the root directory.

Script Details
The script iterates through folders containing images and applies face detection.
Detected faces are outlined with rectangles, and the total number of faces in each image is displayed.
Folder Structure
root/
folder1/
image1.jpg
image2.jpg
...
folder2/
image1.jpg
image2.jpg
...
...
Notes
The face detection results are saved in the root directory as NewImage.jpg. If multiple images are processed, they will overwrite each other, so ensure to move or rename the output accordingly.

The script currently considers only the first face detected in each image.

License
This project is licensed under the MIT License - see the LICENSE file for details.

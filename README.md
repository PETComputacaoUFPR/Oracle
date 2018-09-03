# DEPRECATED < Oracle >

This project was developed to be used by computer science students from Federal University of Parana during an event of the University. It pretends to be a "oracle" giving a random undergraduate degree for students that are going to do an Entry Test for the University. It kind of works like The Sorting Hat.
PETComputacaoUFPR deprecated

# Getting Started

The code was developed based on face recognition API, also available on GitHub: "https://github.com/ageitgey/face_recognition".

Face_recognition uses webcam to run the program. The developers from PETComputacaoUFPR used a Kinect, some parts of the code were modified in order to attend our necessities. It was tested only using CPU, for better performance try using GPU.
The directories "general" and "tests" are from face_recognition and were NOT modified.

In order to run the oracle:
- Get a clone of the project;
- Go to the directory "Code";
- Run the code with "python3 oraculo.py".

# Prerequisites

- python = 3.6.5
- face_recognition
- cv2 = 3.4.2
- freenect = 0.5.3
- PIL 5.1.0
- textwrap

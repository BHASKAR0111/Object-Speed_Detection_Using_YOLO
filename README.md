**Object and Speed Detection using YOLO**

This project implements real-time object detection and speed estimation using the YOLO (You Only Look Once) deep learning model. It can track and detect objects in video feeds, while also estimating their speed based on displacement across frames.

Features
Real-time Object Detection using YOLOv5/YOLoV8

Speed Estimation for moving objects

Multiple Object Tracking

Customizable for video files and live camera feeds

Annotated Output with object labels and speed

Installation
Pre-requisites
Python 3.7+
PyTorch
OpenCV
NumPy

Other dependencies in requirements.txt

Setup

Clone the repository:
git clone https://github.com/BHASKAR0111/Object-Speed_Detection_Using_YOLO.git
cd Object-Speed_Detection_Using_YOLO
Install dependencies:

pip install -r requirements.txt
Download YOLOv5 weights (e.g., yolov5s.pt).

Usage
Run the detection script for a video or live feed:


python detect_speed.py --source video.mp4 --yolo_model yolov5s.pt
Arguments:

--source: Path to video file or webcam (0 for live feed).

--yolo_model: Path to YOLOv5 model weights.

Example Output
Once you run the script, the video will be annotated with:

Bounding boxes around objects

Labels (e.g., "car", "Van")

Speed estimates in km/h or m/s

Example:
The output will look like this:

Contributing
Feel free to contribute to the project! You can:

Fork the repository

Open issues for any bugs or feature requests

Submit pull requests for improvements

License
MIT License

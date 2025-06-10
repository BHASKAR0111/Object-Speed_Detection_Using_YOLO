# Object-Speed_Detection_Using_YOLO

Object and Speed Detection using YOLO
This project implements real-time object detection and speed estimation using the YOLO algorithm. It detects and tracks objects in video feeds and estimates their speed based on movement between frames.

Features
Real-time Object Detection using YOLoV8

Speed Estimation based on object displacement

Multiple Object Tracking in videos

Supports video files and live camera feed

Annotated video output with object labels and speed

Installation
Clone the repository:
git clone https://github.com/yourusername/object-speed-detection-yolo.git
cd object-speed-detection-yolo

Install dependencies:
pip install -r requirements.txt
Download YOLOv5 weights (e.g., yolov5s.pt).

Usage
Run the script with a video or live camera feed:

bash
python detect_speed.py --source video.mp4 --yolo_model yolov5s.pt
--source: Path to video file or webcam (0 for live feed).

--yolo_model: Path to YOLO model weights.

Example Output
The output video will show:

Bounding boxes around objects

Labels (e.g., "car", "person")

Speed estimates (in km/h or m/s)

Contributing
Feel free to fork, open issues, and submit pull requests!

License
MIT License


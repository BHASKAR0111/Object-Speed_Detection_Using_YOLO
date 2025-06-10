import cv2
import pandas as pd
import numpy as np
from ultralytics import YOLO
from tracker_module import Tracker
from datetime import datetime

model = YOLO('yolov8s.pt')
cap = cv2.VideoCapture('veh9.mp4')

with open("coco.txt", "r") as my_file:
    class_list = my_file.read().split("\n")

tracker = Tracker()
counted_ids_up = set()
counted_ids_down = set()
start_times = {}
speeds = {}
fps = cap.get(cv2.CAP_PROP_FPS)
meters_per_pixel = 0.05

valid_y_min = 200
valid_y_max = 450

frame_num = 0

def draw_info(frame, total_up, total_down):
    cv2.putText(frame, f"Going Down: {total_down}", (30, 50),
                cv2.FONT_HERSHEY_SIMPLEX, 1.2, (0, 255, 255), 4)
    cv2.putText(frame, f"Going Up: {total_up}", (700, 50),
                cv2.FONT_HERSHEY_SIMPLEX, 1.2, (0, 255, 255), 4)
    current_time = datetime.now().strftime("%H:%M:%S")
    cv2.putText(frame, f"Time: {current_time}", (430, 40),
                cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 255), 2)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    frame = cv2.resize(frame, (1020, 500))
    frame_num += 1

    results = model.predict(frame, verbose=False)
    detections = pd.DataFrame(results[0].boxes.data).astype("float")

    vehicle_boxes = []
    for _, row in detections.iterrows():
        x1, y1, x2, y2, _, class_id = row
        label = class_list[int(class_id)]
        if label in ['car', 'truck', 'bus', 'motorbike']:
            vehicle_boxes.append([int(x1), int(y1), int(x2), int(y2)])

    tracked = tracker.update(vehicle_boxes)

    for x1, y1, x2, y2, id in tracked:
        cx, cy = int((x1 + x2)/2), int((y1 + y2)/2)
        center = (cx, cy)

        if cy < valid_y_min or cy > valid_y_max:
            continue

        if id not in start_times:
            start_times[id] = (frame_num, center)
        else:
            start_frame, start_center = start_times[id]
            dist_pixels = np.linalg.norm(np.array(center) - np.array(start_center))
            dist_meters = dist_pixels * meters_per_pixel
            time_seconds = (frame_num - start_frame) / fps
            if time_seconds > 0:
                speed = (dist_meters / time_seconds) * 3.6
                speeds[id] = int(speed)

        spd = speeds.get(id, "--")
        color = (0, 0, 255) if isinstance(spd, int) and spd > 60 else (0, 255, 0)

        cv2.rectangle(frame, (x1, y1), (x2, y2), color, 2)
        cv2.putText(frame, f"ID:{id} Speed:{spd} km/h", (x1, y1 - 10),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.6, color, 2)

        if id in start_times:
            _, (sx, sy) = start_times[id]
            if cy < sy and id not in counted_ids_up:
                counted_ids_up.add(id)
            elif cy > sy and id not in counted_ids_down:
                counted_ids_down.add(id)

    draw_info(frame, len(counted_ids_up), len(counted_ids_down))
    cv2.imshow("RGB", frame)

    if cv2.waitKey(1) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()

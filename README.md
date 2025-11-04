# YOLOv8 Object Detection

A minimal real-time object detection project using **Python 3**, **Anaconda**, **OpenCV**, and **Ultralytics YOLOv8**.  
The program performs live object detection on webcam or video input using pre-trained YOLOv8 models.

---

## Overview

This repository demonstrates how YOLOv8 can be used for real-time object detection.  
It provides a simple and clean implementation for running inference, displaying detections, and managing model parameters.

---

## Features

- Uses pre-trained YOLOv8 models (`yolov8n.pt`, `yolov8s.pt`, etc.)
- Works with webcam (`--source 0`) or video file input
- Adjustable confidence threshold
- Real-time frame-by-frame detection
- Exit by pressing `q`

---

## Installation

```bash
git clone https://github.com/omer-akkiyal/yolov8-object-detection
cd yolov8-object-detection
```

Create and activate a virtual environment (recommended):

```bash
conda create -n yolov8-env python=3.11 -y
conda activate yolov8-env
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## Usage

Run with webcam:

```bash
python main.py --source 0
```

Run with a video file:

```bash
python main.py --source path/to/video.mp4
```

Specify model and confidence:

```bash
python main.py --model yolov8s.pt --conf 0.5
```

---

## Project Structure

```
yolov8-object-detection/
├── main.py
├── requirements.txt
└── README.md
```

---

## Tech Stack

- Python 3  
- Anaconda  
- OpenCV  
- Ultralytics YOLOv8  

---

## Possible Extensions

- Save annotated video outputs  
- Add FPS tracking and class-based counting  
- Deploy as a REST API for remote inference  

---

## Author

Developed by [Ömer Akkıyal](https://github.com/omer-akkiyal)  

---

## 📝 License

This project is released under the MIT License.

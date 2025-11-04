import cv2
import argparse
from pathlib import Path
from ultralytics import YOLO


def parse_args():
    parser = argparse.ArgumentParser(
        description="YOLOv8 Object Detection on webcam or video file"
    )
    parser.add_argument(
        "--source",
        type=str,
        default="0",
        help="0 for webcam, or path to a video file (e.g. videos/sample.mp4)",
    )
    parser.add_argument(
        "--model",
        type=str,
        default="yolov8n.pt",
        help="YOLOv8 model path or name (e.g. yolov8n.pt, yolov8s.pt)",
    )
    parser.add_argument(
        "--conf",
        type=float,
        default=0.4,
        help="Confidence threshold for detections",
    )
    return parser.parse_args()


def open_source(source_str: str):
    """
    0 -> webcam
    else -> assume video file path
    """
    if source_str == "0":
        cap = cv2.VideoCapture(0)
    else:
        path = Path(source_str)
        if not path.exists():
            raise FileNotFoundError(f"Source not found: {path}")
        cap = cv2.VideoCapture(str(path))

    if not cap.isOpened():
        raise RuntimeError("Could not open video source.")
    return cap


def main():
    args = parse_args()

    # Load YOLOv8 model
    print(f"Loading model: {args.model}")
    model = YOLO(args.model)

    # Open video source
    cap = open_source(args.source)
    window_name = "YOLOv8 Object Detection"

    print("Press 'q' to quit.")

    while True:
        ret, frame = cap.read()
        if not ret:
            print("No frame received. Exiting...")
            break

        # Run inference
        results = model(frame, conf=args.conf)

        # results[0] -> first image result
        annotated_frame = results[0].plot()  # YOLO built-in drawing

        # Show frame
        cv2.imshow(window_name, annotated_frame)

        # Press q to exit
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

    cap.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()

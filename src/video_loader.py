import cv2
import time
from ball_detector import detect_ball

def load_video(path):
    cap = cv2.VideoCapture(path)
    if not cap.isOpened():
        print("❌ Error: Could not open video.")
        return None
    return cap

def play_video(cap):
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        # Resize frame (optional - match your model if needed)
        frame = cv2.resize(frame, (800, 600))

        # Pass frame to detector
        processed_frame = detect_ball(frame)

        # Show
        cv2.imshow("Smart Table Tennis Analyzer", processed_frame)

        # Exit with 'q'
        if cv2.waitKey(25) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
   cap = load_video("C:/Users/aghog/smart table tennis analyzer new/data/raw/VID-20250430-WA0006.mp4")  # Change if needed
if cap:
        play_video(cap)

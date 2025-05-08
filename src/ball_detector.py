import cv2
import numpy as np
import time

# Globals
trail_points = []
bounce_points = []         # 👈 new: to store bounce locations
prev_center = None
prev_time = None
prev_y = None
bounces = 0

pixels_per_meter = 850 / 2.74  # ≈ 310.22
max_trail_length = 30
max_distance_per_frame = 50

def detect_ball(frame):
    global trail_points, bounce_points, prev_center, prev_time, prev_y, bounces

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    gray = cv2.GaussianBlur(gray, (9, 9), 2)

    circles = cv2.HoughCircles(
        gray,
        cv2.HOUGH_GRADIENT,
        dp=1.2,
        minDist=30,
        param1=100,
        param2=30,
        minRadius=5,
        maxRadius=30
    )

    current_time = time.time()

    if circles is not None:
        circles = np.uint16(np.around(circles))
        for (x, y, r) in circles[0, :1]:
            center = (x, y)

            # Draw the ball
            cv2.circle(frame, center, r, (0, 255, 0), 2)
            cv2.circle(frame, center, 2, (0, 0, 255), 3)

            # Append to trail (only if motion is realistic)
            if prev_center is None or np.linalg.norm(np.array(center) - np.array(prev_center)) < max_distance_per_frame:
                trail_points.append(center)
            if len(trail_points) > max_trail_length:
                trail_points.pop(0)

            # Speed estimation
            if prev_center is not None and prev_time is not None:
                dx = x - prev_center[0]
                dy = y - prev_center[1]
                dist = (dx**2 + dy**2)**0.5
                dt = current_time - prev_time
                speed = dist / dt if dt > 0 else 0

                # Convert to km/h
                speed_mps = speed / pixels_per_meter
                speed_kmph = speed_mps * 3.6

                # Show speed
                cv2.putText(frame, f"Speed: {speed_kmph:.2f} km/h", (20, 40),
                            cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 255), 2)

                # Show HIT
                if speed_kmph > 25 and 300 < y < 460:
                    cv2.circle(frame, center, 30, (0, 255, 255), 3)
                    cv2.putText(frame, "HIT!", (x + 20, y),
                                cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 255), 2)

            prev_center = center
            prev_time = current_time

            # Bounce detection
            if prev_y is not None:
                if prev_y < y and 300 < y < 460:
                    bounces += 1
                    bounce_points.append(center)  # 👈 Save bounce point
                    print(f"🔵 Bounce detected! Total: {bounces}")
            prev_y = y

    # Draw ball trail
    for i in range(1, len(trail_points)):
        cv2.line(frame, trail_points[i - 1], trail_points[i], (255, 255, 0), 2)

    # Draw bounce markers
    for point in bounce_points:
        cv2.circle(frame, point, 20, (255, 0, 255), 2)  # Purple circle

    # Display bounce count
    cv2.putText(frame, f"Bounces: {bounces}", (20, 80),
                cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 100, 255), 2)

    return frame

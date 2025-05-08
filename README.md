Smart Table Tennis Analyzer – Comprehensive Report

Team Members:
Oneyibo Aghogho
Onyeisi Chidiebere

1. Project Overview
The Smart Table Tennis Analyzer is a Python + OpenCV-based tool designed to analyze table tennis videos to provide real-time visual insights into ball movement. The system:
- Detects the ball
- Calculates speed
- Tracks and visualizes trails
- Detects bounces
- Identifies hit moments
- Displays metrics visually on the frame

It was created as part of a Computer Vision and OpenCV course project to demonstrate applied image processing and analysis using Python.

2. Goals
- Build a working system to analyze pre-recorded table tennis gameplay
- Detect the ball frame by frame
- Accurately estimate speed in pixels per second
- Count the number of bounces
- Visualize the ball’s trail
- Circle the ball on impact (hit detection)
- Exclude rally detection
- Show real-time text overlays with calculated stats

3. Tech Stack & Tools
- Language: Python 3.13.2
- Libraries: OpenCV, NumPy
- IDE: Visual Studio Code
- Version Control: Git
- Video Source: Smartphone camera (6 raw .mp4 videos)
- Operating System: Windows 11

4. Folder Structure
smart table tennis analyze/
├── data/
│   └── raw/                  # Contains original .mp4 video files
├── src/
│   ├── ball_detector.py      # Detects, tracks, and annotates ball
│   └── video_loader.py       # Loads video and passes to detector

5. Implementation Summary

video_loader.py
- Loads video using cv2.VideoCapture
- Resizes each frame
- Feeds the frame to detect_ball() function
- Displays output in a real-time OpenCV window

ball_detector.py
- Converts frames to grayscale & blurs for noise reduction
- Uses cv2.HoughCircles() to detect the ball
- Draws trail of ball movement (limited to last 30 positions)
- Detects speed using pixel distance and frame timestamps
- Detects bounces by observing Y-axis changes near the table
- Circles the ball when it's hit (speed spike in playable Y-zone)
- Displays:
  - Speed in pixels per second
  - Bounces
  - Visual markers (trails, hits, bounce rings)

6. Challenges Encountered & Solutions
- Could not open video: Fixed by correcting the relative file path.
- Inaccurate speed values: Normalized pixel-to-meter conversion.
- Cluttered screen with trails: Implemented trail length limiter.
- False bounce events: Improved bounce detection based on Y-coordinate and time gap.

7. GitHub Setup
- Git initialized locally
- First commits made
- GitHub repo created
- Next Steps:
  - Add .gitignore (ignore __pycache__, .vscode/, .mp4)
  - Add README.md
  - Add LICENSE (e.g., MIT)
  - Push to GitHub
  - Tag release (e.g., v1.0)

8. Current Metrics (Sample Output)
- Total Bounces: 2
- Top Speed: 9.71 px/s
- Average Speed: 4.13 px/s
- Total Frames: 1495
- Duration: 41.87 seconds

9. Screenshots
- Real-time overlay of speed and bounces
- Ball trail visual
- Hit detection with yellow ring
- Purple circles marking bounce points

Conclusion
The Smart Table Tennis Analyzer successfully detects, tracks, and analyzes table tennis gameplay from video footage using OpenCV. 
The system effectively handles challenges like detection errors and cluttered displays, resulting in a reliable performance analysis tool.

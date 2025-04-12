## 💤 Drowsiness Detection System using Python, MediaPipe & OpenCV

This project detects eye aspect ratio (EAR) to identify signs of drowsiness using real-time webcam input. An alert sound plays if the user appears drowsy.

---

### 📁 Features

✅ Real-time eye tracking  
✅ Uses MediaPipe (lightweight & modern)  
✅ Alerts user using an audio alarm  
✅ Compatible with Python 3.10+ / 3.12  
✅ No need for dlib or heavy models

---

### 🛠️ Requirements

You need to install the following Python libraries:

```bash
pip install opencv-python mediapipe pygame scipy numpy
```

---

### 🔔 Add Alarm Sound

Place an audio file named `alarm.wav` in the same folder as the script.

- Supported format: `.wav` (Use [Online Converter](https://online-audio-converter.com/) if needed)

---

### 📂 Folder Structure

```
📁 Drowsiness-Detection/
├── alarm.wav
├── drowsiness_detector.py
├── README.md
```

---

### 🧠 How It Works

1. Uses **MediaPipe's FaceMesh** to detect facial landmarks.
2. Tracks specific points around both eyes.
3. Calculates **Eye Aspect Ratio (EAR)**.
4. If EAR is below a threshold (`0.25`) for consecutive frames, it sounds an **ALERT**.

---

### 🚀 Run the Program

```bash
python drowsiness_detector.py
```

- Press **Q** to exit the webcam window.

---

### 📸 Demo Screenshot (optional)

_Add a screenshot like this (if you want):_

```
cv2.putText(frame, "****************ALERT!****************", (10, 30), ...)
```

![demo](https://your-screenshot-link.com) *(replace with actual screenshot URL)*

---

### 💡 Customization

- `thresh = 0.25`: Lower if it's too sensitive, raise if not sensitive enough.
- `frame_check = 20`: How many consecutive drowsy frames before alert triggers.
- Replace `"alarm.wav"` with any alert sound you like (must be `.wav`).

---

### ❓ Troubleshooting

- 🔻 **Music file not found?**
  > Make sure `alarm.wav` is in the same folder as the Python file.

- 🔻 **Webcam not opening?**
  > Ensure no other app is using it, and `cv2.VideoCapture(0)` detects your camera.

---

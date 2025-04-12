import cv2
import mediapipe as mp
from scipy.spatial import distance
from pygame import mixer
import numpy as np

# Initialize music alert
mixer.init()
mixer.music.load("alarm.wav")

# Initialize MediaPipe face mesh
mp_face_mesh = mp.solutions.face_mesh
face_mesh = mp_face_mesh.FaceMesh(static_image_mode=False, max_num_faces=1)

# EAR calculation
def eye_aspect_ratio(eye):
    A = distance.euclidean(eye[1], eye[5])
    B = distance.euclidean(eye[2], eye[4])
    C = distance.euclidean(eye[0], eye[3])
    ear = (A + B) / (2.0 * C)
    return ear

# Left and right eye landmark indices (based on MediaPipe's 468 landmarks)
LEFT_EYE_IDX = [33, 160, 158, 133, 153, 144]
RIGHT_EYE_IDX = [362, 385, 387, 263, 373, 380]

thresh = 0.25
frame_check = 20
flag = 0

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    h, w = frame.shape[:2]
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = face_mesh.process(rgb_frame)

    if results.multi_face_landmarks:
        for face_landmarks in results.multi_face_landmarks:
            landmarks = face_landmarks.landmark

            def get_eye_coords(indexes):
                return np.array([[int(landmarks[i].x * w), int(landmarks[i].y * h)] for i in indexes])

            left_eye = get_eye_coords(LEFT_EYE_IDX)
            right_eye = get_eye_coords(RIGHT_EYE_IDX)

            # Draw eyes
            cv2.polylines(frame, [left_eye], isClosed=True, color=(0, 255, 0), thickness=1)
            cv2.polylines(frame, [right_eye], isClosed=True, color=(0, 255, 0), thickness=1)

            left_ear = eye_aspect_ratio(left_eye)
            right_ear = eye_aspect_ratio(right_eye)
            ear = (left_ear + right_ear) / 2.0

            if ear < thresh:
                flag += 1
                print(flag)
                if flag >= frame_check:
                    cv2.putText(frame, "****************ALERT!****************", (10, 30),
                                cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)
                    cv2.putText(frame, "****************ALERT!****************", (10, 460),
                                cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)
                    mixer.music.play()
            else:
                flag = 0

    cv2.imshow("Drowsiness Detection", frame)
    key = cv2.waitKey(1)
    if key == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()

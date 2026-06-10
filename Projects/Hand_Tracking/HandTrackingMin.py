import cv2 as cv
import mediapipe as mp
import os

BaseOptions = mp.tasks.BaseOptions
HandLandmarker = mp.tasks.vision.HandLandmarker
HandLandmarkerOptions = mp.tasks.vision.HandLandmarkerOptions
VisionRunningMode = mp.tasks.vision.RunningMode

MODEL_PATH = os.path.join(
    os.path.dirname(__file__),
    "hand_landmarker.task"
)

HAND_CONNECTIONS = [
    (0, 1), (1, 2), (2, 3), (3, 4),
    (0, 5), (5, 6), (6, 7), (7, 8),
    (5, 9), (9, 10), (10, 11), (11, 12),
    (9, 13), (13, 14), (14, 15), (15, 16),
    (13, 17), (17, 18), (18, 19), (19, 20),
    (0, 17)
]

options = HandLandmarkerOptions(
    base_options=BaseOptions(
        model_asset_path=MODEL_PATH
    ),
    num_hands=1,
    running_mode=VisionRunningMode.IMAGE
)

cap = cv.VideoCapture(0)
cap.set(cv.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv.CAP_PROP_FRAME_HEIGHT, 480)

with HandLandmarker.create_from_options(options) as landmarker:

    while True:

        success, frame = cap.read()

        if not success:
            continue

        rgb_frame = cv.cvtColor(frame, cv.COLOR_BGR2RGB)

        mp_image = mp.Image(
            image_format=mp.ImageFormat.SRGB,
            data=rgb_frame
        )

        result = landmarker.detect(mp_image)

        if result.hand_landmarks:

            h, w, _ = frame.shape

            for hand_landmarks in result.hand_landmarks:

                for start_idx, end_idx in HAND_CONNECTIONS:

                    x1 = int(hand_landmarks[start_idx].x * w)
                    y1 = int(hand_landmarks[start_idx].y * h)
                    x2 = int(hand_landmarks[end_idx].x * w)
                    y2 = int(hand_landmarks[end_idx].y * h)

                    cv.line(frame,(x1, y1),(x2, y2),(0, 255, 0),1)

                for idx, landmark in enumerate(hand_landmarks):

                    cx = int(landmark.x * w)
                    cy = int(landmark.y * h)

                    cv.circle(frame,(cx, cy),5,(255, 0, 255),-1)
                    cv.putText(frame, str(idx), (cx + 5, cy - 5),cv.FONT_HERSHEY_SIMPLEX,0.4,(255, 255, 255), 1)

                thumb_up = (hand_landmarks[4].x > hand_landmarks[3].x)
                index_up = ( hand_landmarks[8].y < hand_landmarks[6].y )
                middle_up = ( hand_landmarks[12].y < hand_landmarks[10].y)
                ring_up = (hand_landmarks[16].y < hand_landmarks[14].y)
                pinky_up = (hand_landmarks[20].y < hand_landmarks[18].y)
                fingers = [ int(thumb_up),int(index_up), int(middle_up),int(ring_up),int(pinky_up)]

                count = sum(fingers)

                cv.putText(frame,f"Finger States: {fingers}",(10, 30),cv.FONT_HERSHEY_SIMPLEX,0.7,(0, 255, 255),2)
                cv.putText(frame,f"Raised Fingers: {count}",(10, 65),cv.FONT_HERSHEY_SIMPLEX, 0.8,(255, 0, 0), 2)

                if thumb_up:
                    cv.putText(frame,"Thumb -> 1",(10, 100),cv.FONT_HERSHEY_SIMPLEX,0.6,(0, 255, 0),2)
                if index_up:
                    cv.putText(frame,"Index -> 2",(10, 125),cv.FONT_HERSHEY_SIMPLEX, 0.6,(0, 255, 0),2)
                if middle_up:
                    cv.putText(frame,"Middle -> 3",(10, 150),cv.FONT_HERSHEY_SIMPLEX,0.6,(0, 255, 0),2)
                if ring_up:
                    cv.putText(frame,"Ring -> 4",(10, 175),cv.FONT_HERSHEY_SIMPLEX,0.6,(0, 255, 0),2)
                if pinky_up:
                    cv.putText(frame,"Pinky -> 5",(10, 200),cv.FONT_HERSHEY_SIMPLEX,0.6,(0, 255, 0),2)

        cv.imshow("Hand Tracking", frame)

        if cv.waitKey(1) & 0xFF == ord('q'):
            break

cap.release()
cv.destroyAllWindows()
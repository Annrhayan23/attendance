import cv2
import pandas as pd
from datetime import datetime

print("recognize_attendance.py started")

recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.read("trainer.yml")

faceCascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
)

cam = cv2.VideoCapture(0, cv2.CAP_DSHOW)
if not cam.isOpened():
    print("❌ Camera not opening")
    exit()

attendance = []

while True:
    ret, img = cam.read()
    if not ret:
        break

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = faceCascade.detectMultiScale(gray, 1.2, 5)

    for (x,y,w,h) in faces:
        id, confidence = recognizer.predict(gray[y:y+h, x:x+w])

        if confidence < 70:
            time_now = datetime.now().strftime("%H:%M:%S")
            date_now = datetime.now().strftime("%Y-%m-%d")
            attendance.append([id, date_now, time_now])
            label = f"ID {id}"
            color = (0,255,0)
        else:
            label = "Unknown"
            color = (0,0,255)

        cv2.rectangle(img, (x,y), (x+w,y+h), color, 2)
        cv2.putText(img, label, (x,y-10),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.8, color, 2)

    cv2.imshow("Attendance", img)
    if cv2.waitKey(1) == 27:
        break

cam.release()
cv2.destroyAllWindows()

df = pd.DataFrame(attendance, columns=["ID", "Date", "Time"])
df.to_csv("attendance.csv", index=False)

print("✅ Attendance saved to attendance.csv")

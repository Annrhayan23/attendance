import cv2
import os

print("capture_faces.py started")

name = input("Enter your name: ")
user_id = input("Enter numeric ID: ")

# WINDOWS CAMERA FIX
cam = cv2.VideoCapture(0, cv2.CAP_DSHOW)
if not cam.isOpened():
    print("❌ Camera not opening")
    exit()

detector = cv2.CascadeClassifier(
    cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
)

count = 0
os.makedirs("dataset", exist_ok=True)

while True:
    ret, img = cam.read()
    if not ret:
        print("❌ Failed to grab frame")
        break

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = detector.detectMultiScale(gray, 1.3, 5)

    for (x, y, w, h) in faces:
        count += 1
        cv2.imwrite(
            f"dataset/User.{user_id}.{count}.jpg",
            gray[y:y+h, x:x+w]
        )
        cv2.rectangle(img, (x,y), (x+w,y+h), (255,0,0), 2)

    cv2.imshow("Capturing Faces", img)

    # ESC key or 50 images
    if cv2.waitKey(1) == 27 or count >= 50:
        break

cam.release()
cv2.destroyAllWindows()
print("✅ Face images captured successfully")

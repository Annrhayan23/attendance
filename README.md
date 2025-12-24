
# 🎯 Face Recognition Attendance System (Python)

A simple **Computer Vision project** that uses **face recognition** to mark attendance automatically using a webcam. Built with **Python + OpenCV**.

---

## 📌 Features

* Capture face images using webcam
* Train a face recognition model
* Recognize faces in real time
* Automatically mark attendance in CSV file
* Beginner-friendly & VS Code compatible

---

## 🛠️ Tech Stack

* Python 3.x
* OpenCV (opencv-contrib-python)
* NumPy
* Pandas

---

## 📁 Project Structure

```
FaceAttendance/
│── dataset/                 # Stored face images
│── capture_faces.py         # Capture face images
│── train_model.py           # Train face recognition model
│── recognize_attendance.py  # Recognize face & mark attendance
│── trainer.yml              # Trained model (auto-generated)
│── attendance.csv           # Attendance record (auto-generated)
```

---

## ⚙️ Installation

1️⃣ Clone the repository

```bash
git clone https://github.com/Annrhayan23/FaceAttendance.git
cd FaceAttendance
```

2️⃣ Install dependencies

```bash
pip install opencv-contrib-python numpy pandas
```

---

## ▶️ How to Run the Project

### Step 1: Capture Face Images

```bash
python capture_faces.py
```

* Enter your **name** and **numeric ID**
* Webcam opens
* 50 face images are captured automatically

---

### Step 2: Train the Model

```bash
python train_model.py
```

* Trains the face recognition model
* Generates `trainer.yml`

---

### Step 3: Recognize & Mark Attendance

```bash
python recognize_attendance.py
```

* Webcam opens
* Recognized faces are marked present
* Attendance saved in `attendance.csv`
* Press **ESC** to exit

---

## 📄 Sample Attendance CSV

```
ID,Name,Date,Time
23,Ann,2025-12-24,10:30:45
```

---

## 🚀 Use Cases

* College attendance system
* Mini project for Computer Vision
* Python + OpenCV practice
* Resume / GitHub portfolio project

---

## ⚠️ Notes

* Ensure webcam access is enabled
* Use **numeric ID only**
* Good lighting improves accuracy

---

## 📌 Future Improvements

* GUI interface
* Multiple user support
* Cloud attendance storage
* Face mask detection

---

## 👨‍💻 Author

**Ann Rhayan**

---

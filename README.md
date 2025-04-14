# 🧠 OpenCV Workshop

Welcome to the **OpenCV Workshop** organized by **IECSE** and **IEMCT**!  
This session is designed for **beginners** to get a strong foundation in **Computer Vision using OpenCV**.

---

## 🗓️ Workshop Structure

**Total Duration:** ~3 hours  
**Prerequisites:** Basic programming logic (no prior Python/OpenCV knowledge required)

---

## 📚 Agenda

### 1. 🐍 Basics of Python (30–40 mins)
- Variables, loops, functions
- Lists and basic operations
- Reading input/output
- A quick intro to NumPy (arrays and operations)

---

### 2. 📸 Basics of OpenCV (60 mins)

#### 🧱 Basics:
- Reading and displaying images & video
- Drawing shapes and text on images
- Accessing webcam

#### 🎨 Colors and Filters:
- BGR vs HSV color space
- Color masking using `cv2.inRange()`
- Gaussian blur & noise reduction

#### 📐 Shapes and Contours:
- Thresholding & Contour detection
- Drawing and labeling shapes
- Combining color + shape detection

#### 🔢 Bonus: Mathematical Convolution (10–15 mins)
- Manual explanation of how a kernel slides over an image
- Why Gaussian blur works

---

### 🧪 Mini Project: Real-Time Color-Based Object Detection & Traffic Video Analysis

**Objective:**  
Participants will implement two small but impactful projects using OpenCV to consolidate their understanding of core concepts like color detection, masking, contours, and HSV color space.

---

#### 🔴 **Part 1: Real-Time Red Object Detection (Blob Detection)**  
**Goal:** Detect red-colored objects in real time using the webcam and highlight them with bounding boxes.

**Concepts Covered:**
- HSV color space
- Color thresholding with `cv2.inRange`
- Mask creation
- Contour detection
- Drawing bounding boxes
- Area-based filtering

**Expected Output:** Webcam feed where red-colored objects are identified and labeled in real time.

---

#### 🚦 **Part 2: Color Detection in Traffic Video**  
**Goal:** Analyze a recorded video to detect the presence of specific vehicle colors (Red, Yellow, Green) and overlay text showing the detected color.

**Concepts Covered:**
- Reading video files with OpenCV
- Frame-wise HSV conversion
- Multiple color range masking
- Pixel-based detection (`cv2.countNonZero`)
- Video writing (`cv2.VideoWriter`)
- Displaying text overlays on video frames

**Expected Output:** A video where the detected dominant vehicle color is displayed dynamically for each frame.


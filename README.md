# 🧠 Computer Vision & Image Processing – Assignment 1 (EC7212)


## 📋 Overview

This assignment demonstrates fundamental image processing operations using Python, OpenCV, and NumPy. Each task processes a grayscale or color image (`image.jpg`) and saves the results in the `outputs/` folder.

---

## 🛠️ Task Breakdown

### 🔹 Task 1: Intensity Level Reduction  
**Goal:** Reduce the grayscale image's intensity levels from 256 to lower levels like 2, 4, and 8.  
**Script:** `task1_reduce_intensity.py`  
**Method:** Quantize pixel intensities using integer division and multiplication.  
**Output:**  
- `outputs/task1_levels_2.png`  
- `outputs/task1_levels_4.png`  
- `outputs/task1_levels_8.png`

---

### 🔹 Task 2: Spatial Averaging Filter  
**Goal:** Smooth the image using average filters of size 3×3, 10×10, and 20×20.  
**Script:** `task2_average_filter.py`  
**Method:** Use OpenCV’s `cv2.blur()` for uniform filtering.  
**Output:**  
- `outputs/task2_avg_3x3.png`  
- `outputs/task2_avg_10x10.png`  
- `outputs/task2_avg_20x20.png`

---

### 🔹 Task 3: Image Rotation  
**Goal:** Rotate the color image by 45° and 90° angles.  
**Script:** `task3_rotate_image.py`  
**Method:** Generate a rotation matrix using `cv2.getRotationMatrix2D()` and apply with `cv2.warpAffine()`.  
**Output:**  
- `outputs/task3_rotated_45.jpg`  
- `outputs/task3_rotated_90.jpg`

---

### 🔹 Task 4: Block-wise Resolution Reduction  
**Goal:** Simulate lower resolution by averaging non-overlapping blocks of size 3×3, 5×5, and 7×7.  
**Script:** `task4_block_average.py`  
**Method:** Loop through the image using the block size and replace each block with its average value.  
**Output:**  
- `outputs/task4_block_3x3.png`  
- `outputs/task4_block_5x5.png`  
- `outputs/task4_block_7x7.png`

---

## 🚀 How to Run the Code

1. **Clone the repository**
   ```bash
   git clone https://github.com/uvini3974/Computer_Vision_Assigment_1.git
   cd Computer_Vision_Assigment_1

2. **Install Required Libraries**
   ```bash
   pip install opencv-python numpy matplotlib

2. **Run Each Python Script**
   ```bash
   python task1_reduce_intensity.py
   python task2_average_filter.py
   python task3_rotate_image.py
   python task4_block_average.py





   

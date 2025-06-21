
import cv2          
import os          

os.makedirs('outputs', exist_ok=True)

def rotate_image(image, angle):
    
    height, width = image.shape[:2]
    
    center = (width // 2, height // 2)
    
    rotation_matrix = cv2.getRotationMatrix2D(center, angle, scale=1.0)
    
    rotated_image = cv2.warpAffine(image, rotation_matrix, (width, height))
    
    return rotated_image

image = cv2.imread('image.jpg')

if image is None:
    raise FileNotFoundError("image.jpg not found. Please place the file in the same folder.")

for angle in [45, 90]:
    
    result = rotate_image(image, angle)
    
    filename = f'outputs/task3_rotated_{angle}.jpg'
    
    cv2.imwrite(filename, result)
    
    print(f'Saved: {filename}')


import cv2        
import os           

os.makedirs('outputs', exist_ok=True)

def average_filter(image, ksize):
   
    return cv2.blur(image, (ksize, ksize))

image = cv2.imread('image.jpg', cv2.IMREAD_GRAYSCALE)

if image is None:
    raise FileNotFoundError("image.jpg not found. Make sure it's in the same folder.")

for k in [3, 10, 20]:
    
    result = average_filter(image, k)
    
    filename = f'outputs/task2_avg_{k}x{k}.png'
    
    cv2.imwrite(filename, result)
    
    print(f'Saved: {filename}')

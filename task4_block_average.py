
import cv2            
import numpy as np      
import os               

os.makedirs('outputs', exist_ok=True)

def block_average(image, block_size):
 
    height, width = image.shape
    
    output = np.copy(image)

    for i in range(0, height, block_size):
        for j in range(0, width, block_size):
        
            block = image[i:i+block_size, j:j+block_size]
            
            avg_value = np.mean(block).astype(np.uint8)
             
            output[i:i+block_size, j:j+block_size] = avg_value
   
    return output

image = cv2.imread('image.jpg', cv2.IMREAD_GRAYSCALE)

if image is None:
    raise FileNotFoundError("image.jpg not found. Please check the file name and location.")

for block_size in [3, 5, 7]:
   
    result = block_average(image, block_size)

    filename = f'outputs/task4_block_{block_size}x{block_size}.png'

    saved = cv2.imwrite(filename, result)

    if saved:
        print(f"[✓] Saved: {filename}")
    else:
        print(f"[✗] Failed to save: {filename}")

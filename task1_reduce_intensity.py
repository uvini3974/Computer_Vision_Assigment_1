
import cv2                          
import numpy as np                 
import os                         

os.makedirs('outputs', exist_ok=True)

def reduce_intensity_levels(image, levels):
   
    factor = 256 // levels
    
    reduced = (image // factor) * factor
    return reduced

image = cv2.imread('image.jpg', cv2.IMREAD_GRAYSCALE)

if image is None:
    raise FileNotFoundError("image.jpg not found. Please check the file name and location.")

for levels in [2, 4, 8, 16, 32, 64]:
    
    reduced_image = reduce_intensity_levels(image, levels)
    
    filename = f'outputs/task1_levels_{levels}.png'
    
    cv2.imwrite(filename, reduced_image)
    
    print(f'Saved: {filename}')

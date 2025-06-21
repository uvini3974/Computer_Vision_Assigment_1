# Import required libraries
import cv2          # For image processing
import os           # For creating folders and handling files

# Make sure there is an "outputs" folder to save the results
os.makedirs('outputs', exist_ok=True)

# This function applies an average filter of size ksize × ksize to the image
def average_filter(image, ksize):
    # cv2.blur applies a simple average (mean) filter
    return cv2.blur(image, (ksize, ksize))

# Load the image in grayscale mode
image = cv2.imread('image.jpg', cv2.IMREAD_GRAYSCALE)

# Check if the image was successfully loaded
if image is None:
    raise FileNotFoundError("image.jpg not found. Make sure it's in the same folder.")

# Try filtering the image using 3x3, 10x10, and 20x20 average filters
for k in [3, 10, 20]:
    # Apply the average filter
    result = average_filter(image, k)
    
    # Create a file name based on filter size
    filename = f'outputs/task2_avg_{k}x{k}.png'
    
    # Save the filtered image
    cv2.imwrite(filename, result)
    
    # Print a message to confirm the image was saved
    print(f'Saved: {filename}')

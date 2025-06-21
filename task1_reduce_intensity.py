# Import necessary libraries
import cv2                          # For image loading and saving
import numpy as np                 # For numerical operations
import os                          # For handling folders

# Create a folder named "outputs" to save the results
os.makedirs('outputs', exist_ok=True)

# Function to reduce the intensity levels of an image
def reduce_intensity_levels(image, levels):
    # Calculate the factor to reduce intensity (e.g., for 4 levels → factor = 64)
    factor = 256 // levels
    # Divide and multiply to reduce number of levels (quantization)
    reduced = (image // factor) * factor
    return reduced

# Load the image in grayscale mode
image = cv2.imread('image.jpg', cv2.IMREAD_GRAYSCALE)

# Check if the image was loaded correctly
if image is None:
    raise FileNotFoundError("image.jpg not found. Please check the file name and location.")

# Try reducing the image to 2, 4, and 8 intensity levels
for levels in [2, 4, 8]:
    # Call the function to reduce intensity levels
    reduced_image = reduce_intensity_levels(image, levels)
    
    # Create a filename for saving
    filename = f'outputs/task1_levels_{levels}.png'
    
    # Save the resulting image
    cv2.imwrite(filename, reduced_image)
    
    # Print confirmation
    print(f'Saved: {filename}')

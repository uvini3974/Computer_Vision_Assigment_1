# Import required libraries
import cv2              # For image processing
import numpy as np      # For calculations like averaging
import os               # For creating folders

# Make sure the "outputs" folder exists to save the results
os.makedirs('outputs', exist_ok=True)

# Function to apply block-wise averaging
def block_average(image, block_size):
    # Get the height and width of the image
    height, width = image.shape
    
    # Make a copy of the image to store the result
    output = np.copy(image)

    # Go through the image in steps of block_size (non-overlapping blocks)
    for i in range(0, height, block_size):
        for j in range(0, width, block_size):
            # Get the current block of size block_size x block_size
            block = image[i:i+block_size, j:j+block_size]
            
            # Calculate the average value of the block
            avg_value = np.mean(block).astype(np.uint8)
            
            # Set all pixels in the block to the average value
            output[i:i+block_size, j:j+block_size] = avg_value

    # Return the processed image
    return output

# Load the image in grayscale
image = cv2.imread('image.jpg', cv2.IMREAD_GRAYSCALE)

# Check if the image was loaded successfully
if image is None:
    raise FileNotFoundError("image.jpg not found. Please check the file name and location.")

# Try different block sizes: 3x3, 5x5, and 7x7
for block_size in [3, 5, 7]:
    # Apply block average
    result = block_average(image, block_size)

    # Set the filename to save the result
    filename = f'outputs/task4_block_{block_size}x{block_size}.png'

    # Save the image
    saved = cv2.imwrite(filename, result)

    # Print confirmation
    if saved:
        print(f"[✓] Saved: {filename}")
    else:
        print(f"[✗] Failed to save: {filename}")

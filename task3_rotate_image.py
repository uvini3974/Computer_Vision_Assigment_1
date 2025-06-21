# Import required libraries
import cv2          # For image processing
import os           # For file and folder operations

# Create an "outputs" folder to save the rotated images
os.makedirs('outputs', exist_ok=True)

# This function rotates the image by a given angle
def rotate_image(image, angle):
    # Get the height and width of the image
    height, width = image.shape[:2]
    
    # Find the center point of the image (used for rotation)
    center = (width // 2, height // 2)
    
    # Create the rotation matrix using the center and angle
    rotation_matrix = cv2.getRotationMatrix2D(center, angle, scale=1.0)
    
    # Apply the rotation using the matrix
    rotated_image = cv2.warpAffine(image, rotation_matrix, (width, height))
    
    return rotated_image

# Load the original image in color
image = cv2.imread('image.jpg')

# Check if the image is loaded properly
if image is None:
    raise FileNotFoundError("image.jpg not found. Please place the file in the same folder.")

# Rotate the image by 45 degrees and 90 degrees
for angle in [45, 90]:
    # Get the rotated image
    result = rotate_image(image, angle)
    
    # Prepare a filename for saving
    filename = f'outputs/task3_rotated_{angle}.jpg'
    
    # Save the rotated image
    cv2.imwrite(filename, result)
    
    # Print confirmation
    print(f'Saved: {filename}')

import cv2
import os

def resize_images(input_dir, output_dir, target_size):
    # Create the output directory if it doesn't exist
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Get a list of all PNG files in the input directory
    png_files = [file for file in os.listdir(input_dir) if file.lower().endswith('.png')]

    for png_file in png_files:
        # Input file path
        input_path = os.path.join(input_dir, png_file)

        # Output file path
        output_path = os.path.join(output_dir, png_file)

        # Read the image using OpenCV
        img = cv2.imread(input_path)

        # Resize the image
        resized_img = cv2.resize(img, target_size, interpolation=cv2.INTER_LINEAR)

        # Save the resized image to the output directory
        cv2.imwrite(output_path, resized_img)

if __name__ == "__main__":
    # Set your input and output directories
    input_directory = "images/input"
    output_directory = "images/output"

    # Set the target size (width, height) 9:16 aspect ratio (1080, 1920) - (1920, 1080)
    target_size = (1920, 1080)

    # Resize images
    resize_images(input_directory, output_directory, target_size)

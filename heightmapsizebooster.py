#// Input and output paths
input_path = r"yourheightmap.png" # Path to your heightmap image file
output_folder = r"youroutputfolder" # Path to your output directory

#// Packages
import cv2
import numpy as np
import os

#// Ensure the output folder exists
os.makedirs(output_folder, exist_ok=True)

#// Load the heightmap
heightmap = cv2.imread(input_path, cv2.IMREAD_GRAYSCALE)

if heightmap is None:
    print("Error: Unable to load the heightmap. Please check the file path.")
    exit()

#// Get the dimensions of the heightmap
height, width = heightmap.shape

#// Split the heightmap into two based on height values
#// Lower half: values from 0 to 127
#// Upper half: values from 128 to 255
lower_half = np.where(heightmap < 128, heightmap, 128)  #// Keep values < 128, set others to 0
upper_half = np.where(heightmap >= 128, heightmap - 128, 0)  #// Shift values >= 128 down by 128, set others to 0

#// Normalize the lower and upper halves to the full 0-255 range
lower_half_normalized = cv2.normalize(lower_half, None, 0, 255, cv2.NORM_MINMAX)
upper_half_normalized = cv2.normalize(upper_half, None, 0, 255, cv2.NORM_MINMAX)

#// Save the split heightmaps
lower_output_path = os.path.join(output_folder, "lower_half.png")
upper_output_path = os.path.join(output_folder, "upper_half.png")

cv2.imwrite(lower_output_path, lower_half_normalized)
cv2.imwrite(upper_output_path, upper_half_normalized)

print(f"Split heightmaps saved to {output_folder}")

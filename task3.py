import cv2
import easyocr
import matplotlib.pyplot as plt
import numpy as np

# Load the image
img = cv2.imread("photo.jpg")

# Check if the image is loaded correctly
if img is None:
    print("Error: Failed to load image. Make sure the file path is correct.")
    exit()

# Initialize EasyOCR reader
reader = easyocr.Reader(['en'], gpu=False)

# Detect text in the image
text_ = reader.readtext(img)

threshold = 0.25  # Minimum confidence threshold

# Draw bounding boxes and text
for t_, t in enumerate(text_):
    print(t)

    bbox, text, score = t

    if score > threshold:
        (x_min, y_min) = [int(i) for i in bbox[0]]
        (x_max, y_max) = [int(i) for i in bbox[2]]

        cv2.rectangle(img, (x_min, y_min), (x_max, y_max), (0, 255, 0), 3)
        cv2.putText(img, text, (x_min, y_min - 10), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

# Display the image
plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
plt.axis("off")
plt.show()
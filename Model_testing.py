import os
import cv2
import numpy as np
import tensorflow as tf
from tensorflow.keras.preprocessing import image
from tensorflow.keras.applications.mobilenet_v2 import preprocess_input
from PIL import Image

# Load categories
categories = os.listdir("D:/waste_dataset/wastes/train")
categories.sort()

# Load the trained model
path_for_saved_model = "D:/Garbage_V2.h5"
model = tf.keras.models.load_model(path_for_saved_model)
print(model.summary())

def classify_image(frame):
    """Classify an image using the trained model."""
    img = Image.fromarray(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))  # Convert OpenCV BGR to RGB
    img = img.resize((224, 224))

    x = image.img_to_array(img)
    x = np.expand_dims(x, axis=0)
    x = preprocess_input(x)

    pred = model.predict(x)
    categoryValue = np.argmax(pred, axis=1)[0]  # Get the highest probability class

    result = categories[categoryValue]
    return result

# Open Webcam
cap = cv2.VideoCapture(0)  # 0 for default laptop camera

while True:
    ret, frame = cap.read()
    if not ret:
        print("Failed to grab frame")
        break

    # Classify the captured frame
    resultText = classify_image(frame)

    # Display text on the frame
    cv2.putText(frame, resultText, (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

    # Show the image with classification result
    cv2.imshow("Garbage Classification", frame)

    # Press 'q' to exit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release resources
cap.release()
cv2.destroyAllWindows()

import cv2
import numpy as np
import tensorflow as tf
from tensorflow import keras

# Load the pre-trained model
model = keras.models.load_model('model')

# Define the classes
classes = ['hatchback', 'pickup', 'sedan', 'suv']

# Initialize the video capture object
cap = cv2.VideoCapture('videos/surveillance.m4v')
n = 0
# Loop over each frame in the video
while True:
    # Read the next frame
    ret, frame = cap.read()

    # Break the loop if there are no more frames
    if not ret:
        break

    # Preprocess the image
    img = cv2.resize(frame, (224, 224))
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    img = img.astype('float32') / 255.0
    img = np.expand_dims(img, axis=0)

    # Predict the class of the image
    predictions = model.predict(img)
    class_idx = np.argmax(predictions[0])
    class_name = classes[class_idx]

    print('class:', class_name)
    n = n + 1

    # Draw the predicted class on the image
    font = cv2.FONT_HERSHEY_SIMPLEX
    cv2.putText(frame, class_name, (50, 50), font, 1, (0, 255, 0), 2, cv2.LINE_AA)

    # Show the image
    cv2.imshow('Vehicle Classification', frame)

    # Wait for a key press and exit if 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the video capture object and close all windows
cap.release()
cv2.destroyAllWindows()
print(n)

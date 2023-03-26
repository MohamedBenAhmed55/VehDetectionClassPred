
import random
import cv2
import numpy as np
import vehicles
import time
import json
import datetime
from pymongo import MongoClient
import tensorflow as tf
from tensorflow import keras

#Loading the model
model = keras.models.load_model('model')
classes = ['hatchback', 'pickup', 'sedan', 'suv']

cnt_up = 0
cnt_down = 0
r = 0

cap = cv2.VideoCapture("videos/surveillance.m4v")
# cap=cv2.VideoCapture("videos/videoplayback.mp4")
# cap=cv2.VideoCapture("videos/video.mp4")
# cap=cv2.VideoCapture("videos/video1.mp4")

# Get width and height of video

w = cap.get(3)
h = cap.get(4)
frameArea = h * w
areaTH = frameArea / 400

# Lines
line_up = int(2 * (h / 5))
line_down = int(3 * (h / 5))

up_limit = int(1 * (h / 5))
down_limit = int(5 * (h / 5))

print("Red line y:", str(line_down))
print("Blue line y:", str(line_up))
line_down_color = (255, 0, 0)
line_up_color = (255, 0, 255)
pt1 = [0, line_down]
pt2 = [w, line_down]
pts_L1 = np.array([pt1, pt2], np.int32)
pts_L1 = pts_L1.reshape((-1, 1, 2))
pt3 = [0, line_up]
pt4 = [w, line_up]
pts_L2 = np.array([pt3, pt4], np.int32)
pts_L2 = pts_L2.reshape((-1, 1, 2))

pt5 = [0, up_limit]
pt6 = [w, up_limit]
pts_L3 = np.array([pt5, pt6], np.int32)
pts_L3 = pts_L3.reshape((-1, 1, 2))
pt7 = [0, down_limit]
pt8 = [w, down_limit]
pts_L4 = np.array([pt7, pt8], np.int32)
pts_L4 = pts_L4.reshape((-1, 1, 2))

# Background Subtractor // GrayScaling
fgbg = cv2.createBackgroundSubtractorMOG2(detectShadows=True)

# Kernals //decides the nature of the operation
kernalOp = np.ones((3, 3), np.uint8)
kernalOp2 = np.ones((5, 5), np.uint8)
kernalCl = np.ones((11, 11), np.uint)

font = cv2.FONT_HERSHEY_SIMPLEX
cars = []
max_p_age = 5
pid = 1

CTot = 0

while (cap.isOpened()):
    ret, frame = cap.read()
    for i in cars:
        i.age_one()
    fgmask = fgbg.apply(frame)
    fgmask2 = fgbg.apply(frame)

    if ret == True:

        # Binarization // Grayscaling
        ret, imBin = cv2.threshold(fgmask, 200, 255, cv2.THRESH_BINARY)
        ret, imBin2 = cv2.threshold(fgmask2, 200, 255, cv2.THRESH_BINARY)

        # OPening i.e First Erode then dilate
        mask = cv2.morphologyEx(imBin, cv2.MORPH_OPEN, kernalOp)
        # __, mask = cv2.threshold(mask, 254, 255, cv2.THRESH_BINARY)
        mask2 = cv2.morphologyEx(imBin2, cv2.MORPH_CLOSE, kernalOp)

        # new mask for vehicle recognition

        # Closing i.e First Dilate then Erode // transformation d'images
        mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, np.float32(kernalCl))
        mask2 = cv2.morphologyEx(mask2, cv2.MORPH_CLOSE, np.float32(kernalCl))

        # Find Contours
        countours0, hierarchy = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

        # variables to contain the number of each vehicle type

        for cnt in countours0:
            area = cv2.contourArea(cnt)

            if area > areaTH:
                ####Tracking######
                m = cv2.moments(cnt)
                cx = int(m['m10'] / m['m00'])
                cy = int(m['m01'] / m['m00'])
                x, y, w, h = cv2.boundingRect(cnt)
                c = 0

                new = True
                if cy in range(up_limit, down_limit):
                    for i in cars:
                        if abs(x - i.getX()) <= w and abs(y - i.getY()) <= h:
                            new = False
                            i.updateCoords(cx, cy)
                            c = i.getR();
                            class_n=""

                            if i.going_UP(line_down, line_up) == True:
                                cnt_up += 1
                                CTot += c
                                img = cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
                                # cv2.imwrite("cars/carsUP/" + str(cnt_up) + ".png",img[y:y + h - 1, x:x + w])

                            elif i.going_DOWN(line_down, line_up) == True:
                                cnt_down += 1
                                CTot += c
                                # img = cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
                                # cv2.imwrite("cars/carsDOWN/" + str(cnt_up) + ".png",img[y:y + h - 1, x:x + w])
                                img = cv2.resize(frame, (224, 224))
                                img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
                                img = img.astype('float32') / 255.0
                                img = np.expand_dims(img, axis=0)
                                predictions = model.predict(img)
                                class_idx = np.argmax(predictions[0])
                                class_name = classes[class_idx]
                                font = cv2.FONT_HERSHEY_SIMPLEX
                                print('class:', class_name)
                                i.setCl(class_name)
                                class_n = i.getCl()
                                # cv2.putText(frame, class_name, (50, 50), font, 1, (0, 255, 0), 2, cv2.LINE_AA)
                            break
                        if i.getState() == '1':
                            if i.getDir() == 'down' and i.getY() > down_limit:
                                i.setDone()
                            elif i.getDir() == 'up' and i.getY() < up_limit:
                                i.setDone()
                        if i.timedOut():
                            index = cars.index(i)
                            cars.pop(index)
                            del i

                    if new == True:  # If nothing is detected,create new
                        p = vehicles.Car(pid, cx, cy, max_p_age)
                        cars.append(p)
                        pid += 1
                        print(pid)


                # middle red circle
                cv2.circle(frame, (cx, cy), 5, (0, 0, 255), -1)
                # green rectangle
                img = cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
                cv2.putText(img, 'Co2:  ' + str(c) , (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.4, (36, 255, 12), 2)
                # Seperate cars
                roi = frame[x:x + w, y:y + h]
                file_name_path = 'cars/' + str(cnt_up) + '.jpg'
                # cv2.imwrite(file_name_path, roi)

        # shows car id + coordinates
        for i in cars:
            cv2.putText(frame, str(i.getId()), (i.getX(), i.getY()), font, 0.3, i.getRGB(), 1, cv2.LINE_AA)

        # init Car numbers
        str_up = 'UP: ' + str(cnt_up)
        str_down = 'DOWN: ' + str(cnt_down)

        # shows the lines
        frame = cv2.polylines(frame, [pts_L1], False, line_down_color, thickness=2)
        frame = cv2.polylines(frame, [pts_L2], False, line_up_color, thickness=2)
        frame = cv2.polylines(frame, [pts_L3], False, (255, 255, 255), thickness=1)
        frame = cv2.polylines(frame, [pts_L4], False, (255, 255, 255), thickness=1)

        # shows up and down text
        cv2.putText(frame, str_up, (10, 40), font, 0.5, (255, 255, 255), 2, cv2.LINE_AA)
        cv2.putText(frame, str_up, (10, 40), font, 0.5, (0, 0, 255), 1, cv2.LINE_AA)
        cv2.putText(frame, str_down, (10, 90), font, 0.5, (255, 255, 255), 2, cv2.LINE_AA)
        cv2.putText(frame, str_down, (10, 90), font, 0.5, (255, 0, 0), 1, cv2.LINE_AA)

        # opens video window
        cv2.imshow('Frame', frame)
        # cv2.imshow('Mask', mask)
        # cv2.imshow('Mask2', mask2)

        if cv2.waitKey(1) & 0xff == ord('q'):
            break

    else:

        break

carn = cnt_up + cnt_down
avgCo = CTot / carn
date = str(datetime.datetime.now().date())
data = {
    "carcount": carn,
    "Average CO2": avgCo,
    "date": date
}

# json_string = json.dumps(data)
# print(json_string)
#
# client = MongoClient("mongodb://localhost:27017/")
# db = client["mydb"]
# collection = db["mydb"]
# collection.insert_one(data)

cap.release()
cv2.destroyAllWindows()

# To use Inference Engine backend, specify location of plugins:
# source /opt/intel/computer_vision_sdk/bin/setupvars.sh
import cv2 as cv
import numpy as np
import time


BODY_PARTS = {"Wrist": 0,
              "ThumbMetacarpal": 1, "ThumbProximal": 2, "ThumbMiddle": 3, "ThumbDistal": 4,
              "IndexFingerMetacarpal": 5, "IndexFingerProximal": 6, "IndexFingerMiddle": 7, "IndexFingerDistal": 8,
              "MiddleFingerMetacarpal": 9, "MiddleFingerProximal": 10, "MiddleFingerMiddle": 11, "MiddleFingerDistal": 12,
              "RingFingerMetacarpal": 13, "RingFingerProximal": 14, "RingFingerMiddle": 15, "RingFingerDistal": 16,
              "LittleFingerMetacarpal": 17, "LittleFingerProximal": 18, "LittleFingerMiddle": 19, "LittleFingerDistal": 20,
              }

POSE_PAIRS = [["Wrist", "ThumbMetacarpal"], ["ThumbMetacarpal", "ThumbProximal"],
              ["ThumbProximal", "ThumbMiddle"], ["ThumbMiddle", "ThumbDistal"],
              ["Wrist", "IndexFingerMetacarpal"], [
                  "IndexFingerMetacarpal", "IndexFingerProximal"],
              ["IndexFingerProximal", "IndexFingerMiddle"], [
                  "IndexFingerMiddle", "IndexFingerDistal"],
              ["Wrist", "MiddleFingerMetacarpal"], [
                  "MiddleFingerMetacarpal", "MiddleFingerProximal"],
              ["MiddleFingerProximal", "MiddleFingerMiddle"], [
                  "MiddleFingerMiddle", "MiddleFingerDistal"],
              ["Wrist", "RingFingerMetacarpal"], [
                  "RingFingerMetacarpal", "RingFingerProximal"],
              ["RingFingerProximal", "RingFingerMiddle"], [
                  "RingFingerMiddle", "RingFingerDistal"],
              ["Wrist", "LittleFingerMetacarpal"], [
                  "LittleFingerMetacarpal", "LittleFingerProximal"],
              ["LittleFingerProximal", "LittleFingerMiddle"], ["LittleFingerMiddle", "LittleFingerDistal"]]


def coords_handler(points):
    xs = []
    ys = []
    res = []

    # Removing NoneTypes
    for coords in points:
        if coords != None:
            res.append(coords)
        else:
            res.append((0, 0))
    # Seperating xsand ys from points
    for coords in res:
        xs.append(coords[0])
        ys.append(coords[1])

    return xs, ys


def hand_pose(image):

    protoFile = "hand/pose_deploy.prototxt"
    weightsFile = "hand/pose_iter_102000.caffemodel"

    net = cv.dnn.readNet(
        cv.samples.findFile(protoFile),
        cv.samples.findFile(weightsFile)
    )

    cap = cv.VideoCapture(image)

    while True:
        hasFrame, frame = cap.read()
        if not hasFrame:
            cv.waitKey()
            break

        frameWidth = frame.shape[1]
        frameHeight = frame.shape[0]

        inHeight = 368
        inWidth = int((((frameWidth/frameHeight)*inHeight)*8)//8)

        inScale = 1.0 / 255
        thr = 0.1
        time_now = time.time()

        inp = cv.dnn.blobFromImage(
            frame, inScale, (inWidth, inHeight), (0, 0, 0), swapRB=False, crop=False)
        net.setInput(inp)
        out = net.forward()

        print("time taken by network : {:.3f}".format(time.time() - time_now))

        points = []
        for i in range(len(BODY_PARTS)):
            # Slice heatmap of corresponging body's part.
            heatMap = out[0, i, :, :]

            # Originally, we try to find all the local maximums. To simplify a sample
            # we just find a global one. However only a single pose at the same time
            # could be detected this way.
            _, conf, _, point = cv.minMaxLoc(heatMap)
            x = (frameWidth * point[0]) / out.shape[3]
            y = (frameHeight * point[1]) / out.shape[2]

            # Add a point if it's confidence is higher than threshold.
            points.append((int(x), int(y)) if conf > thr else None)

        for pair in POSE_PAIRS:
            partFrom = pair[0]
            partTo = pair[1]
            assert(partFrom in BODY_PARTS)
            assert(partTo in BODY_PARTS)

            idFrom = BODY_PARTS[partFrom]
            idTo = BODY_PARTS[partTo]

            if points[idFrom] and points[idTo]:
                cv.line(
                    frame, points[idFrom], points[idTo], (0, 255, 255), 3)
                cv.ellipse(
                    frame, points[idFrom], (8, 8), 0, 0, 360, (0, 0, 255), cv.FILLED)
                cv.ellipse(
                    frame, points[idTo], (8, 8), 0, 0, 360, (0, 0, 255), cv.FILLED)

        xs, ys = coords_handler(points)

        cv.imshow('OpenPose using OpenCV', frame)
        print("Total time taken : {:.3f}".format(time.time() - time_now))

        print('xs:', xs, '| ys:',  ys)


hand_pose('imgs/hand_5.jpg')

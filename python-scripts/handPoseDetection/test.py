from __future__ import division
import cv2 as cv
import time
import numpy as np

# HAND_PARTS = {
#     "Wrist": 0, "ThumbMetacarpal": 1, "ThumbProximal": 2, "ThumbMiddle": 3, "ThumbDistal": 4,
#     "IndexFingerMetacarpal": 5, "IndexFingerProximal": 6, "IndexFingerMiddle": 7, "IndexFingerDistal": 8,
#     "MiddleFingerMetacarpal": 9, "MiddleFingerProximal": 10, "MiddleFingerMiddle": 11, "MiddleFingerDistal": 12,
#     "RingFingerMetacarpal": 13, "RingFingerProximal": 14, "RingFingerMiddle": 15, "RingFingerDistal": 16,
#     "LittleFingerMetacarpal": 17, "LittleFingerProximal": 18, "LittleFingerMiddle": 19, "LittleFingerDistal": 20,
# }

# POSE_PAIRS = [
#     ["Wrist", "ThumbMetacarpal"],
#     ["ThumbMetacarpal", "ThumbProximal"],
#     ["ThumbProximal", "ThumbMiddle"],
#     ["ThumbMiddle", "ThumbDistal"],
#     ["Wrist", "IndexFingerMetacarpal"],
#     ["IndexFingerMetacarpal", "IndexFingerProximal"],
#     ["IndexFingerProximal", "IndexFingerMiddle"],
#     ["IndexFingerMiddle", "IndexFingerDistal"],
#     ["Wrist", "MiddleFingerMetacarpal"],
#     ["MiddleFingerMetacarpal", "MiddleFingerProximal"],
#     ["MiddleFingerProximal", "MiddleFingerMiddle"],
#     ["MiddleFingerMiddle", "MiddleFingerDistal"],
#     ["Wrist", "RingFingerMetacarpal"],
#     ["RingFingerMetacarpal", "RingFingerProximal"],
#     ["RingFingerProximal", "RingFingerMiddle"],
#     ["RingFingerMiddle", "RingFingerDistal"],
#     ["Wrist", "LittleFingerMetacarpal"],
#     ["LittleFingerMetacarpal", "LittleFingerProximal"],
#     ["LittleFingerProximal", "LittleFingerMiddle"],
#     ["LittleFingerMiddle", "LittleFingerDistal"]
# ]

POSE_PAIRS = [
    [0, 1], [1, 2], [2, 3], [3, 4], [0, 5],
    [5, 6], [6, 7], [7, 8], [0, 9], [9, 10],
    [10, 11], [11, 12], [0, 13], [13, 14], [14, 15],
    [15, 16], [0, 17], [17, 18], [18, 19], [19, 20]
]

font = cv.FONT_HERSHEY_SIMPLEX
font_color = (0, 0, 255)


# def coords_handler(points):


def hand_pose(image):
    protoFile = "hand/pose_deploy.prototxt"
    weightsFile = "hand/pose_iter_102000.caffemodel"

    thr = 0.1

    net = cv.dnn.readNetFromCaffe(protoFile, weightsFile)
    cap = cv.VideoCapture(image)

    while True:
        hasFrame, frame = cap.read()
        if not hasFrame:
            cv.waitKey()
            break

        frameWidth = frame.shape[1]
        frameHeight = frame.shape[0]

        inHeight = 368
        inWidth = int(((frameWidth / frameHeight * inHeight)*8)//8)

        net.setInput(cv.dnn.blobFromImage(
            frame, 1.0 / 255, (inWidth, inHeight), (0, 0, 0), swapRB=False, crop=False))

        output = net.forward()

        # aspect_ratio = frameWidth/frameHeight
        t = time.time()
        print("time taken by network : {:.3f}".format(time.time() - t))

        # Empty list to store the detected keypoints
        points = []
        for i in range(22):
            # confidence map of corresponding body's part.
            heatMap = output[0, i, :, :]
            heatMap = cv.resize(heatMap, (frameWidth, frameHeight))

            # Find global maxima of the probMap.
            _, conf, _, point = cv.minMaxLoc(heatMap)

            x = point[0]
            y = point[1]

            # Add the point to the list if the conf is greater than the threshold
            points.append((int(x), int(y)) if conf > thr else None)

        # Draw Skeleton
        for pair in POSE_PAIRS:
            partFrom = pair[0]
            partTo = pair[1]

            # idFrom = HAND_PARTS[partFrom]
            # idTo = HAND_PARTS[partTo]

            if points[partFrom] and points[partTo]:
                cv.line(
                    frame, points[partFrom], points[partTo], (0, 255, 255), 2)
                cv.circle(
                    frame, points[partFrom], 8, (0, 0, 255), thickness=-1, lineType=cv.FILLED)
                cv.circle(
                    frame, points[partTo], 8, (0, 0, 255), thickness=-1, lineType=cv.FILLED)

                # cv.putText(frame, str(partTo),
                #            points[idTo], font, 0.5, font_color, 1, cv.LINE_AA)
                # cv.putText(frame, str(partFrom),
                #            points[idFrom], font, 0.5, font_color, 1, cv.LINE_AA)

        cv.imshow('Output-Skeleton', frame)

        img_name = '{}_points.jpg'.format(image)
        cv.imwrite('imgs/points/'+img_name, frame)

        print("Total time taken : {:.3f}".format(time.time() - t))

        break


if __name__ == "__main__":

    hand_pose('imgs/right-frontal.jpg')

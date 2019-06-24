import time
import os
import cv2 as cv

cap = cv.VideoCapture(0)


def cap_screen():

    t_start = time.time()
    t_end = t_start + 2

    while time.time() < t_end:
           # Capture frame-by-frame
        ret, frame = cap.read()

        # Turns the diplay 90 degrees and changes color
        #frame2 = cv2.cvtColor(np.rot90(frame), cv2.COLOR_BGR2RGB)
        #frame2 = pygame.surfarray.make_surface(frame2)
        # Displays the time remaing, before picture is taken, and evaluaed
        #t_now = time.time()

    # Once the while loop breaks, write img
    if not os.path.exists('imgs'):
        os.makedirs('imgs')

    img_name = "imgs/hand.jpg"
    cv.imwrite(img_name, frame)

    return img_name


if __name__ == "__main__":
    cap_screen()

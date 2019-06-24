# "ThumbDistal": 4
# "IndexFingerDistal": 8
# "MiddleFingerDistal": 12
# "RingFingerDistal": 16
# "LittleFingerDistal": 20
# middel = distal-1
from playsound import playsound


def finger_counter(x, y):
    res = "An error has occured"
    if (x[4] > x[3]) and (y[8] < y[7]) and (y[12] < y[11]) and (y[16] < y[15]) and (y[20] < y[19]):
        #playsound('audio/mambofive.mp3')
        res = 5
    elif (x[4] < x[3]) and (y[8] < y[7]) and (y[12] < y[11]) and (y[16] < y[15]) and (y[20] < y[19]):
        #playsound('audio/4minutes.mp3')
        res = 4
    elif (x[4] > x[3]) and (y[8] < y[7]) and (y[12] < y[11]) and (y[16] > y[15]) and (y[20] > y[19]):
       # playsound('audio/threebirds.mp3')
        res = 3
    elif (x[4] < x[3]) and (y[8] < y[7]) and (y[12] < y[11]) and (y[16] > y[15]) and (y[20] > y[19]):
       # playsound('audio/wuuhuu.mp3')
        res = 2
    elif (x[4] < x[3]) and (y[8] < y[7]) and (y[12] > y[11]) and (y[16] > y[15]) and (y[20] > y[19]):
        #playsound('audio/thunder.mp3')
        res = 1
    elif (x[4] < x[3]) and (y[8] < y[7]) and (y[12] > y[11]) and (y[16] > y[15]) and (y[20] < y[19]):
       # playsound('audio/thunder.mp3')
        res = 666
    else:
        res = "I do not yet recognized this gesture"
    return res

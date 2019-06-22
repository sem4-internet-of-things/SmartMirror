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
        playsound('audio/mambofive.mp3')
        res = "Five fingers detected"
    elif (x[4] < x[3]) and (y[8] < y[7]) and (y[12] < y[11]) and (y[16] < y[15]) and (y[20] < y[19]):
        playsound('audio/4minutes.mp3')
        res = "Four fingers detected"
    elif (x[4] > x[3]) and (y[8] < y[7]) and (y[12] < y[11]) and (y[16] > y[15]) and (y[20] > y[19]):
        playsound('audio/threebirds.mp3')
        res = "Three fingers detected"
    elif (x[4] < x[3]) and (y[8] < y[7]) and (y[12] < y[11]) and (y[16] > y[15]) and (y[20] > y[19]):
        playsound('audio/wuuhuu.mp3')
        res = "Two fingers detected"
    elif (x[4] < x[3]) and (y[8] < y[7]) and (y[12] > y[11]) and (y[16] > y[15]) and (y[20] > y[19]):
        playsound('audio/thunder.mp3')
        res = "One finger detected"
    elif (x[4] < x[3]) and (y[8] < y[7]) and (y[12] > y[11]) and (y[16] > y[15]) and (y[20] < y[19]):
        playsound('audio/thunder.mp3')
        res = "ROCK detected"
    else:
        res = "I do not yet recognized this gesture"
    return res

# "ThumbDistal": 4
# "IndexFingerDistal": 8
# "MiddleFingerDistal": 12
# "RingFingerDistal": 16
# "LittleFingerDistal": 20
# middel = distal-1
import os

def finger_counter(res):
    if (res=="5"):
        os.system("omxplayer audio/mambofive.mp3")
        res = "Five fingers detected"
    elif (res=="4"):
        os.system("omxplayer audio/4minutes.mp3")
        res == "Four fingers detected"
    elif (res=="3"):
        os.system("omxplayer audio/threebirds.mp3")
        res = "Three fingers detected"
    elif (res=="2"):
        os.system("omxplayer audio/wuuhuu.mp3")
        res = "Two fingers detected"
    elif (res=="1"):
        os.system("omxplayer audio/thunder.mp3")
        res = "One finger detected"
    elif (res=="666"):
        os.system("omxplayer audio/thunder.mp3")
        res = "ROCK detected"
    else:
        os.system("omxplayer audio/sad_trombone.mp3")
        res = "I do not yet recognized this gesture"
    return res
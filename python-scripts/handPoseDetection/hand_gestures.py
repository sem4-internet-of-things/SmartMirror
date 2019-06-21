#"ThumbDistal": 4
#"IndexFingerDistal": 8
#"MiddleFingerDistal": 12
#"RingFingerDistal": 16
#"LittleFingerDistal": 20
# middel = distal-1
from playsound import playsound

def finger_counter(x,y):
    res="An error has occured"
    if (x[4] > x[3]) and (y[8] < y[7]) and (y[12] < y[11]) and (y[16] < y[15]) and ( y[20] < y[19]):
        playsound('imperial_march.wav')
        res="Five fingers detected"
    elif (x[4] < x[3]) and (y[8] < y[7]) and (y[12] < y[11]) and (y[16] < y[15]) and ( y[20] < y[19]):
        playsound('Aaron_Smith_-_Dancin_KRONO_Remix')
        res="Four fingers detected"
    elif (x[4] > x[3]) and (y[8] < y[7]) and (y[12] < y[11]) and (y[16] > y[15]) and ( y[20] > y[19]):
        playsound('song3.mp3')
        res="Three fingers detected"
    elif (x[4] < x[3]) and (y[8] < y[7]) and (y[12] < y[11]) and (y[16] > y[15]) and ( y[20] > y[19]):
        playsound('Aaron_Smith_-_Dancin_KRONO_Remix')
        res="Two fingers detected"
    elif (x[4] < x[3]) and (y[8] < y[7]) and (y[12] > y[11]) and (y[16] > y[15]) and ( y[20] > y[19]):
        playsound('Aaron_Smith_-_Dancin_KRONO_Remix')
        res="One finger detected"
    else:
        res="I do not yet recognized this gesture"
    return res
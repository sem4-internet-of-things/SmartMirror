import requests
import base64
import song_selector
import cap_screen

URL = "http://169.254.233.99:5000/"

#  first, encode our image with base64
def run():
    with open(cap_screen.cap_screen(), "rb") as imageFile:
        img = base64.b64encode(imageFile.read())

    response = requests.post(URL, data={"img":img})
    print(response.text)
    res=song_selector.finger_counter(response.text)
    print(res)
    print("done")
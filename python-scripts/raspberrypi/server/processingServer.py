from flask import Flask, request
import testhand2
import cv2
import numpy as np
from flask_cors import CORS
import base64
from PIL import Image

app = Flask(__name__)
CORS(app)

    
@app.route('/', methods = ['POST'])
def api_message():
    imageString = base64.b64decode(request.form["img"])
    nparr = np.frombuffer(imageString, np.uint8)
    data = cv2.imdecode(nparr, cv2.IMREAD_ANYCOLOR);

    img2 = Image.fromarray(data, 'RGB')
    b, g, r = img2.split()
    im = Image.merge("RGB", (r, g, b))
    im.save('my.jpg')

    res=testhand2.hand_pose("my.jpg")
    return str(res)
app.run(host= '169.254.233.99')
    
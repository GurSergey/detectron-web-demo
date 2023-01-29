import flask
from flask import Flask, make_response
import numpy as np
from detectron2class import Detectron2Class
import cv2
initialized = False

app = Flask(__name__)

detectron = Detectron2Class()
initialized = True


@app.route('/get_status', methods=['GET'])
def get_status():
    return {'initialized': initialized}


@app.route('/detect', methods=['POST'])
def get_answer():

    file = flask.request.files['imagefile'].read()
    file_bytes = np.fromstring(file, np.uint8)
    image = cv2.imdecode(file_bytes, cv2.IMREAD_UNCHANGED)

    output_image = detectron.detect_image(image)
    retval, buffer = cv2.imencode('.png', output_image)
    response = make_response(buffer.tobytes())
    response.content_type = 'image/png'
    return response


app.debug = False
app.run(host='0.0.0.0', port=5005)

from doodlewar2 import generate_sketch
from flask import Flask, send_file, request
import cv2
import numpy as np
import os
from flask_cors import CORS, cross_origin

# Initialize the Flask application
app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'


@app.route("/")
def home():
    return "Flask Server is Running!!!"
# route http posts to this method


@app.route('/convert_image', methods=['POST'])
def convert_image():
    try:
        file = request.files['image']
        file.save("temp.png")
        print("file saved...")
        processed_image = generate_sketch()
        print(processed_image)
        return processed_image
    except Exception as error:
        print(error)
        return "Custom Error!!!!!!"


# start flask app
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)

# try:
#     image = request.files['image']
#     print(image)
#     if 'image' not in request.files:
#         return "missing image attribute"
#     return send_file(image)
# except Exception as error:
#     return error
# return send_file(img, mimetype='image/png')

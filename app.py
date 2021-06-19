from doodlewar2 import generate_sketch
from flask import Flask, send_file, request
import cv2

# Initialize the Flask application
app = Flask(__name__)


@app.route("/")
def home():
    return "Flask Server is Running!!!"
# route http posts to this method


@app.route('/convert_image', methods=['POST'])
def convert_image():
    try:
        image = request.files['image']
        print(image)
        processed_image = generate_sketch(image)
        if 'image' not in request.files:
            return "missing image attribute"
        return "All ok with image"
    except Exception as error:
        print(error)
        return "Custom Error!!!!!!"


# start flask app
app.run(port=5000)


# try:
#     image = request.files['image']
#     print(image)
#     if 'image' not in request.files:
#         return "missing image attribute"
#     return send_file(image)
# except Exception as error:
#     return error
# return send_file(img, mimetype='image/png')

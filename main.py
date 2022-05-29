import os
import random

import flask
from flask import request, send_file, jsonify

app = flask.Flask(__name__)


@app.route('/api/gachi/random', methods=['GET'])
def get_random_gachi_image():
    data = request.json
    if data['format'] == 'jpg':
        images = [image_name for image_name in os.listdir('images') if image_name.endswith('.jpg')]
    elif data['format'] == 'gif':
        images = [image_name for image_name in os.listdir('images') if image_name.endswith('.gif')]
    elif data['format'] == 'any':
        images = [image_name for image_name in os.listdir('images')]
    else:
        return jsonify({'status': 'error', 'info': 'Incorrect format'})
    file = random.choice(images)
    return send_file(f'images/{file}')


app.run('127.0.0.1', 3698, debug=True)

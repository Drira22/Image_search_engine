from flask import Flask, render_template, request, redirect, url_for,jsonify,send_from_directory
import os 
import numpy as np
from PIL import Image
import io
from feature_image_ex import extract_features 
from cosine_search import search_similar_images



app=Flask(__name__)



@app.route('/data/images/<path:filename>', methods=['GET'])
def serve_image(filename):
    return send_from_directory('data/images', filename)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    # Read the image
    file = request.files['file']
    image_to_process = Image.open(file.stream)

    # Process the image and extract features
    feature_vector = extract_features(image_to_process)  
    similar_images = search_similar_images(feature_vector)

    return jsonify({'similarImages': similar_images})

if __name__ == "__main__":
    app.run(debug=True)
import os
from app import app
from PIL import Image
from skimage.io import imread
from skimage.color import rgb2gray
from skimage.filters import threshold_otsu
from flask import render_template, request
from skimage.metrics import structural_similarity

app.config['INITIAL_FILE_UPLOADS'] = 'app/static/uploads'
app.config['EXISTING_FILE'] = 'app/static/original'
app.config['GENERATED_FILE'] = 'app/static/generated'


@app.route('/', methods=['GET', 'POST'])
def index():

    if request.method == 'GET':
        return render_template('index.html')

    if request.method == 'POST':
        # Get Uploaded(Test) Image
        file = request.files['file_upload']
        test_img = Image.open(file)

        # Resize Test Image
        test_img = test_img.resize((250, 160))

        # Save Test Image in jpg format
        test_img.convert('RGB').save(os.path.join(
            app.config['INITIAL_FILE_UPLOADS'], 'test_image.jpg'))

        # Open Images in SKImage
        original_img = imread(os.path.join(app.config['EXISTING_FILE'], 'original.jpg'))
        test_img = imread(os.path.join(app.config['INITIAL_FILE_UPLOADS'], 'test_image.jpg'))

        # Convert Images to Grayscale
        original_img = (rgb2gray(original_img) * 255).astype('uint8')
        test_img = (rgb2gray(test_img) * 255).astype('uint8')

        # Calculate Structural Similarity Index
        score, diff_img = structural_similarity(original_img, test_img, full=True)
        diff_img = (diff_img * 255).astype("uint8")

        # Generate binary image using OTSU Threshold
        binary_img = diff_img <= threshold_otsu(diff_img)

        # Save Generated Images
        Image.fromarray(diff_img).save(os.path.join(app.config['GENERATED_FILE'], 'diff_image.jpg'))
        Image.fromarray(binary_img).save(os.path.join(app.config['GENERATED_FILE'], 'binary_image.jpg'))

        if score < 0.75:
            return render_template('index.html', result='Card is Tampered')
        else:
            return render_template('index.html', result='Card is NOT Tampered')

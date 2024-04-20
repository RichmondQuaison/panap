<a name="readme-top"></a>

<div align="center">

# __Pan Card Tampering Detection__

### Built Using
  
[![Python][python-shield]][python-url]
[![html-css-js][html-css-js-shield]][html-css-js-url]
[![Flask][flask-shield]][flask-url]
[![ScikitImage][scikit-image-shield]][scikit-image-url]

Visit the <a href="https://pancard-tampering-detector.onrender.com">Web Application</a> deployed on render

</div>

## __About__
<p align="justify">
This is a simple application to detect tampering of Pan Cards using <a href="https://en.wikipedia.org/wiki/Structural_similarity#:~:text=The%20structural%20similarity%20index%20measure,the%20similarity%20between%20two%20images.">Structural Similarity Index Measure (SSIM)</a>. It is used to measure similarity of two images. A Pan Card is tampered if it's SSIM value with original Pan Card template is low.

Original Pan Card template: https://www.thestatesman.com/wp-content/uploads/2019/07/pan-card.jpg

Tampered Pan Card Sample: https://assets1.cleartax-cdn.com/s/img/20170526124335/Pan4.png

See the implementation details with <a href="https://github.com/Pranav-Nagpure/Pan-Card-Tampering-Detection-NB">IPython Notebook</a>
</p>

## __Getting Started__

This Project is Built With [![Anaconda][anaconda-shield]][anaconda-url] [![VSCode][vscode-shield]][vscode-url] [![Render][render-shield]][render-url]

### __Installation__
To use the app on local machine, open Anaconda Prompt and run the following commands:

1. Clone the Repository
```sh
git clone https://github.com/Pranav-Nagpure/Pan-Card-Tampering-Detection.git
```

2. Change Working Directory
```sh
cd Pan-Card-Tampering-Detection
```

3. If needed create a Virtual Environment and activate it
```sh
conda create -n environment_name python=3.10
conda activate environment_name
```

4. Install the requirements
```sh
python -m pip install -r requirements.txt
```

5. Run the App
```sh
python app.py
```

6. Open the URL generated in a browser to use the App

7. You can use images in the sample_images folder

<p align="right">
(<a href="#readme-top">back to top</a>)
</p>

[python-shield]: https://raw.githubusercontent.com/Pranav-Nagpure/Support-Repository/master/images/python-shield.png "Python"
[python-url]: https://www.python.org

[html-css-js-shield]: https://raw.githubusercontent.com/Pranav-Nagpure/Support-Repository/master/images/html-css-js-shield.png
[html-css-js-url]: https://html.spec.whatwg.org "HTML | CSS | JavaScript"

[anaconda-shield]: https://raw.githubusercontent.com/Pranav-Nagpure/Support-Repository/master/images/anaconda-shield.png
[anaconda-url]: https://www.anaconda.com "Anaconda"

[vscode-shield]: https://raw.githubusercontent.com/Pranav-Nagpure/Support-Repository/master/images/vscode-shield.png
[vscode-url]: https://code.visualstudio.com "VSCode"

[render-shield]: https://raw.githubusercontent.com/Pranav-Nagpure/Support-Repository/master/images/render-shield.png
[render-url]: https://render.com "Render"

[flask-shield]: https://raw.githubusercontent.com/Pranav-Nagpure/Support-Repository/master/images/flask-shield.png "Flask"
[flask-url]: https://flask.palletsprojects.com

[scikit-image-shield]: https://raw.githubusercontent.com/Pranav-Nagpure/Support-Repository/master/images/scikit-image-shield.png "Scikit-Image"
[scikit-image-url]: https://scikit-image.org
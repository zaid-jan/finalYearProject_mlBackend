import os
from flask import Flask, flash, request, redirect, url_for, session
from werkzeug.utils import secure_filename
# from flask_cors import CORS, cross_origin
import logging

logging.basicConfig(level=logging.INFO)

logger = logging.getLogger('HELLO WORLD')



UPLOAD_FOLDER = 'F:/Sources/Projects/finYearProject/mlBackend'
ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/upload', methods=['POST'])
def fileUpload():
    target=os.path.join(UPLOAD_FOLDER,'videos')
    if not os.path.isdir(target):
        os.mkdir(target)
    logger.info("welcome to upload`")
    print(request.files)
    file = request.files['video'] 
    filename = secure_filename(file.filename)
    destination="/".join([target, filename])
    file.save(destination)
    session['uploadFilePath']=destination
    response="upload"
    return response

if __name__ == "__main__":
    app.secret_key = os.urandom(24)
    app.run(debug=True,host="0.0.0.0",use_reloader=False)

# flask_cors.CORS(app, expose_headers='Authorization')
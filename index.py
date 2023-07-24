from flask import Flask, render_template, request,flash
from werkzeug.utils import secure_filename
import os


UPLOAD_FOLDER = 'static'
ALLOWED_EXTENSIONS = {'png', 'webp', 'png', 'jpg', 'jpeg', 'gif'}

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def proscessing():
    pass

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')



@app.route('/edit', methods=["GET","POST"])
def edit():
    if request.method == "POST":
        return "POST request is here"
    
        if 'file' not in request.files:
            flash('No file part')
            return "error"
        file = request.files['file']
   
        if file.filename == '':
            flash('No selected file')
            return "error no selected file"
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return redirect(url_for('download_file', name=filename))
            #process image()
            return render_template("index.html")
                   
    return render_template('index.html')

if __name__=="__main__":
    app.run(debug=True)
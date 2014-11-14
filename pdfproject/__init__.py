import processing
import os
import fnmatch
from flask import Flask, Response, request, session, g, redirect, url_for, abort, render_template, flash, send_from_directory,jsonify
from werkzeug import secure_filename
import shelve
import socket
import re
ALLOWED_EXTENSIONS = set(['pdf','PDF'])

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = '/PDFProject/pdfproject/uploads'

def allowed_file(filename):
    return '.' in filename and \
        filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS
def findFile(pattern, path):
    result = []
    for root, dirs, files in os.walk(path):
        for name in files:
            if fnmatch.fnmatch(name, pattern):
                result.append(os.path.join(root, name))
    return result
@app.route("/")
def hello():
	return render_template("layout.html")

@app.route("/start/")
def homeprint():
	return render_template("start.html")

@app.route("/process/",methods=['GET','POST'])
def upload_file():
	print 'upload file'
	try:
		os.stat(app.config['UPLOAD_FOLDER'])
	except:
		os.mkdir(app.config['UPLOAD_FOLDER'])
	if request.method == 'POST':
		file = request.files['uploadFile']
		print type(file.stream)
		print 'filename' + file.filename
		if file and allowed_file(file.filename):
			print 'allowing file'
			filename = secure_filename(file.filename)
			file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
			print "saved?"
			processing.process(os.path.join(app.config['UPLOAD_FOLDER'], filename))
			print "ran?"
			return redirect(url_for('uploaded_file', filename=filename)) #"upload success" #redirect(url_for('uploaded_file',filename=filename))
		return "No!"
	return "NO"	

@app.route('/uploads/<filename>')
def uploaded_file(filename):
	p = filename+'.*jpg$'
	patt = re.compile(p)
	result = []
	for file in os.listdir("/PDFProject/pdfproject/uploads"):
		if patt.match(file):
			result.append(file)
	return render_template(processed,result=result)#send_from_directory(app.config['UPLOAD_FOLDER'], filename)

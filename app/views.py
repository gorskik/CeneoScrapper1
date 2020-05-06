from app import app
from flask import render_template, request, redirect, url_for
from flaskext.markdown import Markdown
from app.forms import ProductForm
Markdown(app)

app.config['SECRET_KEY'] = 'TajemniczyMysiSprzęt'

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
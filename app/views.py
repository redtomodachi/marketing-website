from app import app
from flask import render_template


@app.route('/')
def home():
    return render_template('home.html')

@app.route('/functionalities')
def functionalities():
    return render_template('functionalities.html')

@app.route('/workdesc')
def workdesc():
    return render_template('workDesc.html')

@app.route('/developers')
def developers():
    return render_template('developers.html')

@app.route('/demo')
def demo():
    return render_template('demo.html')



@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html'), 404
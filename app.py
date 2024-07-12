from flask import Flask, render_template
from database import get_data

app = Flask(__name__)
@app.route('/')
def index():
    return render_template('index.html')
@app.route('/about')
def about():
    data = get_data()
    return render_template('about.html', data=data)
@app.route('/selfindro')
def selfindro():
     return render_template('selfindro.html')
if __name__=="main":
        app.run()
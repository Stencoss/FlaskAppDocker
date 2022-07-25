# Main file
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')
    
@app.route('/secondPage')
def secondPage():
    return render_template('secondPage.html')


if __name__ == '__main__': 
    app.run(debug=True)
#!/usr/bin/python3

from flask import Flask, render_template

app = Flask(__name__)

# Replace route in 4-hbnb.py
@app.route('/4-hbnb')
def hbnb():
    return render_template('4-hbnb.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

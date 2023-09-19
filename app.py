# import libraries
from flask import Flask, render_template, request

# instanciation of app Flask
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

# variables environment
if __name__ == '__main__':
    app.run(debug=True, port=3300)
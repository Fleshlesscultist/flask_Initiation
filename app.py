# import libraries
from flask import Flask, render_template, request

# instanciation of app Flask
app = Flask(__name__)

# Route home
@app.route('/')
def home():
    return render_template('index.html', title="L")

# Route form
@app.route('/form', methods=["POST", "GET"])
def form():
    data = 242
    if request.method == 'POST':
        age = request.form['age']
        sex = request.form['sex']
        pclass = request.form['class']
        print(age, sex, pclass)

    result = data
    return render_template('form.html', result=result, title="resultat")

# variables environment
if __name__ == '__main__':
    app.run(debug=True, port=3300)
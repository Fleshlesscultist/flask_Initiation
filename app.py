# import libraries
from flask import Flask, render_template, request
import pandas as pd

# import model
from models.classifier import model

# instanciation of app Flask
app = Flask(__name__)

# Route home
@app.route('/')
def home():
    return render_template('index.html', title="L")

# Route form
@app.route('/form', methods=["POST", "GET"])
def form():
    if request.method == 'POST':
        age = request.form['age']
        if age.isnumeric():
            age = int(age)
        else:
            return render_template('form.html', title="resultat")
        sex = int(request.form['sex'])
        pclass = int(request.form['class'])
        data = {'age':age,
                'sex':sex,
                'pclass':pclass}
        df = pd.DataFrame(data, index=[0])
        resultat = model.survie(df)
        print(resultat)
        
        return render_template('form.html', result=resultat, title="resultat")
    else:
        return render_template('form.html', title="resultat")

# variables environment
if __name__ == '__main__':
    app.run(debug=True, port=3300)
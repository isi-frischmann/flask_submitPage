from flask import (Flask, render_template, request)

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/submitPage', methods=['GET', 'POST'])
def submitPage():
    name = request.form['name'] 
    language = request.form['language'] 
    location = request.form['location'] 
    comment = request.form['comment'] 
    return render_template('submitPage.html', name = name, language = language, location = location, comment = comment)


app.run(debug = True)
from flask import Flask,render_template
app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('index.html')

@app.route('/ankur')
def harry():
    return 'Hello, Ankur Maurya.Here is your first API... !'

app.run(debug=True)

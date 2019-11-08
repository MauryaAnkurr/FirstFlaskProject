from flask import Flask,render_template
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')
@app.route('/ankur')
def secondcode():
    return 'Hello, Ankur Maurya.Here is your first API... !'

app.run(debug=True)

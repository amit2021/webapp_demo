from flask import Flask

app = Flask(__name__)

@app.route('/amit')
def hello():
    return 'hello world'


app.run(host='0.0.0.0',debug=True)
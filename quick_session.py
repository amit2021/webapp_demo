from flask import Flask,session

app=Flask(__name__)

app.secret_key='amit'


@app.route('/setuser/<user>')
def setuser(user : str) ->str:
    session['user']=user
    return 'user value set to: '+session['user']

@app.route('/getuser')
def getuser() ->str:
    return 'user value is currently set to:  '+session['user']


if __name__=='__main__':
    app.run(host='0.0.0.0',debug=True)
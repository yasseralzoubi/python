from flask import Flask

app =Flask(__name__)


@app.route('/')
def Hello_world():
    return 'Hello World!'

@app.route("/Champion")
def print_champion():
    return "Champion!"


@app.route('/say/<name>')
def say_name(name):
    return "Hi " + name + "!"


@app.route('/repeat/<word>/<num>')
def print_repeat(word,num):
    return (word +"  ")* int(num)




if __name__=="__main__":
    app.run(debug=True)
from flask import Flask , render_template

app = Flask(__name__)

@app.route('/play')
def print_play():
    return render_template('index.html',times=3)

@app.route('/play/<int:times>')
def print_playtimes(times):
    return render_template('index.html',times=times)


@app.route('/play/<int:times>/<color>')
def print_playtimescolor(times,color):
    return render_template('index.html',times=times,color=color)
if __name__=="__main__":
    app.run(debug=True)
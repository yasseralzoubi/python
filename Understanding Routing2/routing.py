from flask import Flask ,render_template
app=Flask("__name__")

@app.route('/')
def print_hello():
    return render_template('index.html')
@app.route('/Champion')
def print_champion():
    return render_template('Champion!.html')
@app.route('/say/<name>')
def print_hi_flask(name):
    return render_template('names.html',name=name)

@app.route('/repeat/<int:times>/<name>')
def print_repeat(times,name):
    return render_template('repeat.html',times=times,name=name)







# @app.route('/repeat/<int:times>/<name>')
# def print_repeat(times,name):
#     return render_template('repeat.html',times=times,name=name)




if __name__==('__main__'):
    app.run(debug=True)
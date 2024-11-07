from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def display():
    return render_template("checkboard.html",rows=8,cols=8,color1='black',color2='white')

@app.route('/<int:x>')
def display_4(x):
    return render_template("checkboard.html",rows=x,cols=x,color1='black',color2='white')   


@app.route('/<int:x>/<int:y>')
def display_x_y(x,y):
    return render_template("checkboard.html",rows=x,cols=y,color1='black',color2='white')   

@app.route('/<int:x>/<int:y>/<color1>/<color2>')
def display_x_y_color(x , y , color1 ,color2):
    return render_template("checkboard.html", rows=x , cols=y , color1=color1 , color2=color2)  


if __name__ == "__main__":
    app.run(debug=True)
from flask import Flask, render_template,request
app = Flask(__name__)


@app.route('/')
def survey():
    return render_template("information.html")


@app.route('/result',methods=['POST'])#post should be capital 
def User_survey():
    #key                         value
    yourname = request.form['your_name']
    location =request.form['Location']
    language = request.form['language']
    comment = request.form['comment']


    return render_template("submition.html", name = yourname , location=location, language=language, comment =comment)




if __name__ == "__main__":
    app.run(debug=True)
from flask import Flask, render_template,request
app = Flask(__name__)


@app.route('/')
def users():
    context = [
        {"first_name":"Micjael","last_name":"Choi"},
        {"first_name":"John","last_name":"Supsupin"},
        {"first_name":"mark","last_name":"Guillen"},
        {"first_name":"KB","last_name":"Tonel"},
    ]


    return render_template("index.html",context=context)




# @app.route('/result',methods=['POST'])#post should be capital 
# def User_survey():
#     #key                         value
#     yourname = request.form['your_name']
#     location =request.form['Location']
#     language = request.form['language']
#     comment = request.form['comment']


#     return render_template("submition.html", name = yourname , location=location, language=language, comment =comment)




if __name__ == "__main__":
    app.run(debug=True)
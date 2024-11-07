from flask import Flask, render_template,request
app = Flask(__name__)


@app.route('/')
def display():
    return render_template("submit_info.html")


@app.route('/checkout',methods=['POST'])#post should be capital 
def checkout():
    #key                         value
    your_name = request.form['yourname']
    your_id =request.form['yourid']
    Strawberry = request.form['strowberry']
    Rospberry = request.form['rospberry']
    Apple = request.form['apple']
    


    return render_template("display_inf.html", Name = your_name , ID=your_id , Order_str=Strawberry,Oreder_Ros=Rospberry,Order_Apple=Apple )




if __name__ == "__main__":
    app.run(debug=True)
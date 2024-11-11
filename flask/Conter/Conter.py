from flask import Flask, render_template,request,session
app = Flask(__name__)
app.secret_key = 'your_secret_key_here' #why i have written this here


@app.route('/')                    #when the route is empty
def Counter():                     #it will execute this function
    if 'hello' not in session:     #here i making sure that session is empty
                                   #hello is key and it will related with Html file writen by jinja
        session['hello']=1         #if it is empty , it will equal 1 and save it in a session
    else:                          #if it is not empty
        session['hello']+=1        #it will increment by 1 , and save at a session
    return render_template("index.html",hello=session['hello'])   #value will retern to the brawser as it saved in session

@app.route('/destroy_session')    #when the route is destroy_session
def destroy():                    #it will execute this function 
    session.clear()               #this function will clear the session
    return render_template("index.html")              #and retern to the brawser


if __name__ == "__main__":
    app.run(debug=True)
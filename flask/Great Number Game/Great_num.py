from flask import Flask, render_template, request, session
import random

app = Flask(__name__)
app.secret_key = 'your_secret_key_here'  # مطلوب لاستخدام الجلسات بشكل آمن


@app.route('/')
def great_number():
    # إعداد رقم عشوائي إذا لم يتم إعداده مسبقًا
    if "rand_num" not in session:
        session["rand_num"] = random.randint(1, 100)
    return render_template("index.html")


@app.route('/result', methods=['POST'])
def result_of_game():
    guess = int(request.form['guess'])  # الحصول على التخمين من المستخدم
    rand_number = session["rand_num"]

    if guess > rand_number:
        session['message'] = 'Too high!'
    elif guess < rand_number:
        session['message'] = 'Too low!'
    else:
        session['message'] = f"{guess} was the number! You've guessed it correctly!"

    return render_template("index.html", message=session['message'])


if __name__ == "__main__":
    app.run(debug=True)
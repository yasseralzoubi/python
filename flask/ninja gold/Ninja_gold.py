from flask import Flask, render_template, request, redirect, session
import random

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # تأكد من وضع مفتاح سري

@app.route('/')
def index():
    # تهيئة الجلسة إذا لم تكن موجودة
    if 'gold' not in session:
        session['gold'] = 0
    if 'activities' not in session:
        session['activities'] = []
    
    return render_template('index.html')

@app.route('/process_money', methods=['POST'])
def process_money():
    place = request.form['place']
    min_gold = int(request.form['min-gold'])
    max_gold = int(request.form['max-gold'])
    
    earned_gold = random.randint(min_gold, max_gold)  # يتم حساب الذهب العشوائي

    # تحديث قيمة الذهب في الجلسة
    session['gold'] += earned_gold

    # إضافة النشاط إلى الجلسة
    activity = f"Entered a {place} and earned {earned_gold} gold!"
    session['activities'].append(activity)
    
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)

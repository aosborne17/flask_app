from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_required, current_user
# from answers import answers

main = Blueprint('main', __name__)

# answers = {"Q1":  "Class", "Q2":  "def", "Q3": "print()", "Q4":  "=="}
answers = ["Class", "def", "print()", "=="]

@main.route('/')
def index():
    return render_template('index.html')


@main.route('/profile')
@login_required
def profile():
    return render_template('profile.html', name=current_user.name)


@main.route('/quiz', methods=["GET", "POST"])
@login_required
def quiz():
    if request.method == 'POST':
        score = 0
        if request.form['q1'] == answers[0]:
            score += 1
        elif request.form['q2'] == answers[1]:
            score += 1
        elif request.form['q3'] == answers[2]:
            score += 1
        elif request.form['q4'] == answers[3]:
            score += 1
        with open("templates/answers.html", 'a') as f:
            f.write(f"Good Work, You Scored {score} questions correctly!")
        return redirect(url_for('answers'))
    return render_template('quiz.html')


@main.route('/answers')
@login_required
def answers():
    return render_template("answers.html")

from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_required, current_user
from answers import answers

main = Blueprint('main', __name__)


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
        if request.form['q1'] != answers.get("Q1"):
            flash("INCORRECT")
        else:
            score += 1
        return redirect(url_for('answers'))
    return render_template('quiz.html')


@main.route('/answers')
@login_required
def answers():
    return render_template("answers.html")

from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('profile.html',name = "ankit",is_Topper = True,marks = [85,90,78,92])
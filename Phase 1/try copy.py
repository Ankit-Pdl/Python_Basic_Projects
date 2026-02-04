from flask import Flask, request,session,redirect,url_for,Response


app = Flask(__name__)
app.secret_key = "yunisha"

@app.route('/', methods =['POST','GET'])
def login():
  if request.method =='POST':
    username = request.form.get("username")
    password = request.form.get("passwords")

    if username =='ankit' and password =='123':
      session['user']  = username
      return redirect(url_for("Welcome"))
    else:
      return Response(
        "Invalid credendentials.Try again",
        mimetype="text/plain"
      )
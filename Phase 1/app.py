from flask import Flask, request, redirect, url_for, Response, session, render_template

app = Flask(__name__)
app.secret_key = "supersecret"

# homepage (login)
@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        # debugging
        print(f"__Debug__")
        print(f"User Entered: {username}")
        print(f"password entered {password}")
        print(f"Matched username?: {username =='ankit'}")
        print(f"Matched Password?: {password}")
        

        if username == "ankit" and password == "ap":
            session["user"] = username
            return redirect(url_for("welcome"))
        else:
            return Response(
                "Invalid credentials. Try again" )

    return render_template("login.html") 

@app.route("/welcome")
def welcome():
    print("SESSION IN WELCOME:", session)
    if "user" in session:
        return render_template("welcome.html",user = session["user"])
        
    return redirect(url_for("login"))

@app.route("/logout")
def logout():
    session.pop("user", None)
    return redirect(url_for("login"))

if __name__ == "__main__":
    app.run(debug=True)
from flask import Flask,render_template,request

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("feedback.html")



@app.route("/feedback",methods=["GET","POST"])
def feedback():
    if request.method =="POST":
        name = request.form.get("name")
        feedback = request.form.get("message")
        return render_template("thankyou.html",user=name , message=feedback )
    return render_template("feedback.html")  

if __name__ == "__main__":
    app.run(debug=True)
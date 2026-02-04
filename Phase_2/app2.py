from flask import Flask, render_template,request

valid_users ={
    'admin': 'Passw0rd',
    'unsaa': 'cutie123',
    'john_doe': 'John@2024'
}
app = Flask(__name__)
@app.route('/')
def home():
    return render_template('login.html')

if __name__ == '__main__':
    app.run(debug=True)

@app.route('/submit', methods=['POST'])
def submit():
    username = request.form['username']    
    password = request.form['password']

    if username in valid_users and valid_users[username] == password:
        return render_template('welcome.html', username=username)
    else:
        return "❌ Invalid credentials. Please try again."
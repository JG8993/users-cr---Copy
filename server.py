from flask import Flask, render_template, request, redirect
from user import User
app = Flask(__name__)

@app.route("/")
def index():
    return render_template('create.html')

@app.route('/read')
def create():
    return render_template("read.html", users=User.get_all())


@app.route('/create_user', methods=["POST"])
def create_user():
    print(request.form)
    User.save(request.form)
    return redirect('/read')


@app.route('/delete_users')
def delete_users():
    print(request.form)
    User.delete_all(request.form)
    return redirect ('/read')

if __name__ == "__main__":
    app.run(debug=True)
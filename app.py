from flask import Flask, app,render_template , request,redirect,url_for

app=Flask(__name__)

@app.route('/')
def hello_admin():
    return render_template('index.html')



@app.route('/jam',methods=["GET", "POST"])
def hello_admin1():
    name1 = request.form['name']
    print(name1)
    return redirect(url_for("kit",jam=name1))

@app.route('/kit/<jam>')
def kit(jam):
    return "You are in"


if __name__ == '__main__':
    app.run(debug=True)
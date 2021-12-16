
from flask import Flask, render_template, request, redirect, session, url_for
app = Flask(__name__)
app.secret_key = 'its a secret!'

@app.route('/')
def counter():
    if 'counter' in session:
        session['counter'] += 1
    else:
        session['counter'] = 0
    return render_template("counter.html")

@app.route('/destroy')
def destroy():
    session.clear()
    return redirect("/")

@app.route('/reset')
def reset():
    if 'counter' in session:
        session['counter'] = 0
    return redirect("/")

@app.route('/plustwo')
def plustwo():
    if 'counter' in session:
        session['counter'] += 1
    return redirect("/")

@app.route('/youradd', methods=['POST'])
def youradd():
    print(request.form)
    session['counter'] += int(request.form["add_number"]) - 1
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)
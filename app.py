from flask import Flask, request, render_template, session, redirect, url_for, flash
import json
import db

app=Flask(__name__)



@app.route("/login",methods=['GET','POST'])
def login():
    if request.method=='GET':
        #print request.args.get('nextpage')
        return render_template("login.html",next=request.args.get('nextpage',"/login"))
    elif request.form['button']=='login':
        user = request.form['username']
        pw = request.form['password']
        next = request.form['nextpage']
        result = db.checkCredentials(user,pw)
        if result==False:
            flash("Invalid username or password")
            return render_template("login.html",next=request.args.get('nextpage',"/login"))
        session['user']=user
        return redirect(next)
    else:
        user = request.form['username']
        pw = request.form['password']
        next = request.form['nextpage']
        result = db.addUser(user,pw)
        if result==None:
            flash("Couldn't add user");
            return render_template("login.html",next=request.args.get('nextpage',"/login"))
        else:
            flash("Log in using new username and password")
            return render_template("login.html",next=request.args.get('nextpage',"/login"))


@app.route("/logout")
def logout():
    session.pop('user',None)
    return redirect("/");
@app.route("/")
def index():
    if 'user' not in session:
        session['nextpage']=request.path
        return redirect(url_for('login',nextpage=request.path))
    return render_template("index.html")


@app.route("/f")
def f():
    return render_template("base.html")
if __name__=="__main__":
    app.secret_key = "the secret key"
    app.debug=True
    app.run(host="0.0.0.0",port=5000)

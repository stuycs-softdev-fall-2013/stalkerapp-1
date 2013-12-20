from flask import Flask, request, render_template, session, redirect, url_for
import json

app=Flask(__name__)



@app.route("/login",methods=['GET','POST'])
def login():
    if request.method=='GET':
        #print request.args.get('nextpage')
        return render_template("login.html",next=request.args.get('nextpage',"/login"))
    else:
        print request.form.keys()
        user = request.form['username']
        pw = request.form['password']
        next = request.form['nextpage']
        print next
        session['user']=user
        return redirect(next)


@app.route("/register")
def register():
    return "REGISTER PAGE"


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

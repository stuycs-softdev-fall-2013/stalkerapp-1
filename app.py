from flask import Flask, request, render_template, session, redirect, url_for
import json

app=Flask(__name__)



@app.route("/loginform",methods=['GET','POST'])
def loginform():
    if request.method=='GET':
        print request.args.get('nextpage')
        return render_template("login.html")
    else:
        return "DOING THE LOGIN"

@app.route("/login")
def login():
    user = request.args.get('username',"")
    pw = request.args.get("password","")

    if user=="z" and pw=="z":
        session['user']='z'
        return json.dumps({'user':"z"})
    return json.dumps({'user':""})

@app.route("/register")
def register():
    return "REGISTER PAGE"


@app.route("/")
def index():
    session['nextpage']=request.path
    print request.path
    return redirect(url_for('loginform',nextpage=request.path))



@app.route("/f")
def f():
    return render_template("base.html")
if __name__=="__main__":
    app.secret_key = "the secret key"
    app.debug=True
    app.run(host="0.0.0.0",port=5000)

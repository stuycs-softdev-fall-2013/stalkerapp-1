##flask imports cc
from flask import Flask, request, render_template, session, redirect, url_for, flash

# ihelloltin imports
import json

# local packages
import db


app=Flask(__name__)
# The secret key MUST be set out side of the main if at the bottom
app.secret_key = "the secret key"
 
################################################################################
#
#        Web page routes
#
################################################################################


@app.route("/login",methods=['GET','POST'])
def login():
    """
    print a login page and either handle a login or register from the page.
    
    use the nextpage argument in the request to forward to another page once
    login is succesful (and store 'user' in the session)
    """
    if request.method=='GET':
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
        # register
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
    """
    """
    session.pop('user',None)
    return redirect("/");

@app.route("/track")
def track():
    """
    go to the map page showing users currently logged in - mostly javascript in track.js
    """
    if 'user' not in session:
        session['nextpage']=request.path
        return redirect(url_for('login',nextpage=request.path))
    return render_template("track.html",PAGENAME=request.path,user=session['user'])

@app.route("/stalk")
def stalk():
    """
    does nothing right now
    """
    if 'user' not in session:
        session['nextpage']=request.path
        return redirect(url_for('login',nextpage=request.path))
    return render_template("placeholder.html",PAGENAME=request.path)

@app.route("/")
def index():
    """
    Home page - doesn't do anything right now
    """
    if 'user' not in session:
        session['nextpage']=request.path
        return redirect(url_for('login',nextpage=request.path))
    return render_template("index.html")


################################################################################
#
#        AJAX page routes
#
################################################################################

@app.route("/getCurrents")
def getCurrents():
    """
    return a list of the current people on the system
    fields include: name, timestamp, geo
    geo includes: type (point), coordinates (lat,lng)
    """
    return db.getCurrents()


@app.route("/updateCurrent")
def updateCurrent():
    """
    modify database so it stores the current users current location
    Must be logged in (hence the 'user' if up top
    """
    if 'user' not in session:
        session['nextpage']=request.path
        return redirect(url_for('login',nextpage=request.path))
    name=session['user']
    lat = request.args.get('lat')
    lng = request.args.get('long')
    print lat,lng
    loc=[lat,lng]
    db.updateCurrent(name,loc)
    return json.dumps(True)



################################################################################
#
#        main
#
################################################################################

if __name__=="__main__":
    app.debug=True
    app.run(host="0.0.0.0",port=5000)



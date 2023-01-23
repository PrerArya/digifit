from flask import Flask,render_template,request,redirect,url_for,flash,redirect
import pickle

#media for the project
import os
prerna = os.path.join('static','pic.png')
prerna2 = os.path.join('static','Untitled.png')
prerna3 = os.path.join('static','wardrobe.png')
video = os.path.join('static','DigitalWardrobe.mp4')
prerna4 = os.path.join('static','BUUTON.png')
prerna5 = os.path.join('static','start.png')
prerna6=os.path.join('static','home.jpeg')

#create flask app
app = Flask(__name__)

#path for the pages
@app.route('/')
def index():
    return render_template("index.html",img = prerna2,img1 = prerna,img2 = prerna3,vid=video)

@app.route('/home')
def home() :
    return render_template("home.html",title='home',button=prerna4,home=prerna6)  


database={'prerna':'12345678'}
@app.route('/login',methods=['POST','GET'])
def login():
    name1=request.form['username']
    pwd=request.form['password']
    if name1 not in database:
        return render_template(login.html,info='Invalid Username')
    if [name1]!=pwd:
            return render_template(login.html,info='Invalid Password')  
    else:
        return render_template('home.html',name=name1)    


@app.route("/createyourcloset")
def createyourcloset():
    return render_template("createyourcloset.html",start=prerna5)     

@app.route("/opennewcloset")
def opennewcloset():
    return render_template("opennewcloset.html")

if __name__=="__main__":
        
    app.run(debug=True)
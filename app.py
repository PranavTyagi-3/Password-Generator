from flask import Flask,render_template,request
import random

app=Flask(__name__)


def genr(size,cb1,cb2):
    sp=['!','@','#','$','%','^','&','_','~','?']
    passwrd=[]
    global passwrdstr
    passwrdstr=""
    if cb1==0 and cb2==0:
        s=size//2
        for i in range(s):
            passwrd.append(chr(random.randint(97,122)))
        for i in range(size-s):
            passwrd.append(chr(random.randint(65,90)))

    if cb1==1 and cb2==0:
        s=size//3
        for i in range(s):
            random.shuffle(sp)
            passwrd.append(sp[0])
        for i in range(s):
            passwrd.append(chr(random.randint(65,90)))
        for i in range(size-(s*2)):
            passwrd.append(chr(random.randint(97,122)))

    if cb1==0 and cb2==1:
        s=size//3
        for i in range(s):
            passwrd.append(random.randint(0,9))
        for i in range(s):
            passwrd.append(chr(random.randint(65,90)))
        for i in range(size-(s*2)):
            passwrd.append(chr(random.randint(97,122)))
            
    if cb1==1 and cb2==1:
        s=size//4
        for i in range(s):
            passwrd.append(random.randint(0,9))
        for i in range(s):
            random.shuffle(sp)
            passwrd.append(sp[0])
        for i in range(s):
            passwrd.append(chr(random.randint(65,90)))
        for i in range(size-(s*3)):
            passwrd.append(chr(random.randint(97,122)))
    random.shuffle(passwrd)
    for i in passwrd:
        passwrdstr=passwrdstr+str(i)

    return (passwrdstr)

@app.route('/',methods=("GET","POST"))
def index():
    if request.method=="POST":
        cb=[0,0]
        option = request.form.getlist('options')
        s=request.form['size']
        try:
            s=int(s)
        except:
            s=8
        for i in option:
            if i=='1':
                cb[0]=1
            elif i=='2':
                cb[1]=1
        generated=genr(s,cb[0],cb[1])
        return render_template('index.html',gen=generated)
    return render_template('index.html')

if __name__=="__main__":
    app.run(debug=True)


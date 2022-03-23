from math import ceil
from flask import Flask, render_template 
app = Flask(__name__)    
@app.route('/')         
def hello_world():
    return render_template ("index.html",row=8,col=8) 


@app.route('/<num>')         
def hello_world2(num):
    num=int(num)
    return render_template ("index.html",row=8,col=num)

@app.route('/<num>/<num2>')         
def hello_world3(num,num2):
    num=int(num)
    num2=int(num2)
    return render_template ("index.html",row=num2,col=num)

@app.route('/<num>/<num2>/<color1>/<color2>')         
def hello_world4(num,num2,color1,color2):
    num=int(num)
    num2=int(num2)
    return render_template ("index.html",row=num2,col=num,c1=color1,c2=color2)

if __name__=="__main__":   
    app.run(debug=True)
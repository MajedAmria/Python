from flask import Flask, render_template,request,redirect, session
app = Flask(__name__)
app.secret_key = 'keep it secret, keep it safe'



@app.route('/')
def create_user():
  
    if session:
       session["time"] += 1
    else:
        session["time"] = 1
        
   
    
    return render_template("index.html")	


@app.route("/clear",methods=['POST'])
def show_visitor():
    if request.form["botton"]=="two":
        session["time"] += 1
    elif request.form["botton"]=="clear":
       session.clear()
    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)


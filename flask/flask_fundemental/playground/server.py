from flask import Flask, render_template
app = Flask(__name__)

@app.route('/play')
def index():
    return render_template('index.html',number=3,colorch='blue')
@app.route('/play/<num>')
def div(num):
    
    return render_template('index.html',number=int(num),colorch='blue')
@app.route('/play/<num>/<color>')
def bv(num,color):
    
    return render_template('index.html',number=int(num),colorch=color)
	
if __name__=="__main__":
    app.run(debug=True)
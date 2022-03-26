from flask import Flask, render_template,request
app = Flask(__name__)
# our index route will handle rendering our form
@app.route('/')
def index():
    return render_template("index.html")
@app.route('/users', methods=['POST'])
def create_user():
    print("Got Post Info")
    print(request.form)
    name_from_form = request.form['name']
    location_from_form=request.form['location']
    language_from_form = request.form['language']
    return render_template("show.html", name=name_from_form, location=location_from_form,language=language_from_form)
if __name__ == "__main__":
    app.run(debug=True)
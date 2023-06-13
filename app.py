from flask import Flask, render_template, request, flash

app = Flask(__name__)
app.secret_key = "majhjhki98arpig_MUDMAN888"

@app.route("/")
def index2():
    return render_template("index.html")
@app.route("/hello")
def index():
    flash("WHats your name")
    return render_template("index.html")

@app.route("/greet", methods=['POST', 'GET'])
def greeter():
	flash("Hi " + str(request.form['name_input']) + ", great to see you!")
	return render_template("index.html")
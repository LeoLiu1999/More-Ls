from flask import Flask,render_template
import util.occupation.py

app = Flask(__name__)

@app.route("/")
def landing():
	return 'Hi there, go to <a href="localhost:5000/occupations"> occupations </a>'

@app.route("/occupations")
def occupation_temp():

if app.__name__ == "__main__":
	app.debug = True
	app.run()
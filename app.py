from flask import Flask,render_template
import util.occupation as jobs

app = Flask(__name__)

#This is the landing page
@app.route("/")
def landing():
	return 'Hi there, go to <a href="http://localhost:5000/occupations"> occupations </a>'

#This is the actual page
@app.route("/occupations")
def occupation_temp():
	csv = jobs.make_dict_from_csv('occupations.csv')
	random_job = jobs.random_job(csv)
	return render_template('occupations.html',job_dict=csv,random_job=random_job)

if __name__ == "__main__":
	app.debug = True
	app.run()
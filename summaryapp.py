import flask
from flask_cors import CORS
from flask import render_template, url_for, redirect, flash
from summarizer import Summarizer


app = flask.Flask(__name__)
app.secret_key = b'*****' #your key
CORS(app)

model = Summarizer()


@app.route("/summarize", methods=["POST", "GET"])
def summarize():
	data = dict()
	data["success"] = False

	if flask.request.method == "POST":
		if flask.request.form.get("context"):
			context = flask.request.form.get("context")
			answer = 'not found, please try again!'
			if flask.request.form.get("btn")=='ratio':
				result = model(context, ratio=0.3)
				answer = ''.join(result)
			if flask.request.form.get("btn")=='sentence':
				# result = model(context, ratio=0.3)
				answer = model(context, num_sentences=5)



			# return flask.jsonify(data)
			return render_template("summaryPage.html", answer=answer, context=context)
		else:
			flash("No content to summarize!", "warning")
			return render_template("summaryPage.html")
	if flask.request.method == "GET":
		return render_template("summaryPage.html")	

if __name__ == '__main__':
	print("Starting web service")
	app.run(host='localhost', port="45000", debug=True)





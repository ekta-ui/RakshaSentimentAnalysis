from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from flask import *

app=Flask(__name__)
analyser = SentimentIntensityAnalyzer()

@app.route("/")
def home():
    return render_template('home.html')

@app.route("/analyze",methods = ['GET'])
def analyze():
	text = request.args.get('text')
	score = analyser.polarity_scores(text)
	score_compound=round(score["compound"]*100,2)
	score_positive =round(score["pos"]*100,2)
	score_negative=round(score["neg"]*100,2)
	score_neutral=round(score["neu"]*100,2)

	if(score_compound<0):
		score_compound=0
	

	return render_template('home.html', 
                            score_positive =round(score["pos"]*100,2),
                            score_negative=round(score["neg"]*100,2),
                            score_neutral=round(score["neu"]*100,2),
                            score_compound=score_compound
                            )

@app.route("/analyze/api",methods = ['GET'])
def analyze_api():
	text = request.args.get('text')
	score = analyser.polarity_scores(text)
	return jsonify(
    	score_positive =score["pos"]*100,
        score_negative=score["neg"]*100,
        score_neutral=score["neu"]*100,
        score_compound=score["compound"]*100
        )

app.run(debug=True)
app.run(host='0.0.0.0', port=8080)
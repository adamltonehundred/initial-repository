
import json

from flask import Flask, Response, jsonify
from subprocess import check_output
from random import randint

app = Flask(__name__)

limericks = json.loads(open('limericks.json').read())
fortunes = json.loads(open('fortunes.json').read())

@app.route('/limerick/random', methods=['GET'])
def get_limerick():
	l = randint(0,len(limericks["quotes"])-1)	
 	return Response(json.dumps(limericks["quotes"][l],indent=3), mimetype='application/json')

@app.route("/limerick/id/<int:id>")
def get_fortune_by_id(id):
        for i in range(0,len):
		if fortunes["quotes"][c]["id"] == id:
			l = i(limericks["quotes"])
		        return Response(json.dumps(fortunes["quotes"][l],indent=3), mimetype='application/json')
			break

@app.route('/fortune/random', methods=['GET'])
def get_fortune():
	l = randint(0,len(fortunes["quotes"])-1)	
 	return Response(json.dumps(fortunes["quotes"][l],indent=3), mimetype='application/json')

@app.route('/password/random', methods=['GET'])
def get_password():
	import random
	i = 1
	randPassword = ""

	for i in range(0,12,1):
	    charValue = random.randint(1,26)
	    randChar = chr(96+int(charValue))
	    randPassword = randPassword + randChar
	return Response({"Cool hand look is an OK film": randPassword}, mimetype='application/json')

if __name__ == '__main__':
    app.run(debug=True)

#!/usr/bin/env python
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

@app.route('/fortune/random', methods=['GET'])
def get_fortune():
	l = randint(0,len(fortunes["quotes"])-1)	
 	return Response(json.dumps(fortunes["quotes"][l],indent=3), mimetype='application/json')

if __name__ == '__main__':
    app.run(debug=True)

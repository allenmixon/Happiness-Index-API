from flask import Flask, jsonify, abort
import json

app = Flask(__name__)

#load data from file
with open('happiness-index-seed-data.json') as json_file:
    json_data = json.load(json_file)

#print (json_data)

@app.route('/happiness-index', methods=['GET'])
def get_all():
	return jsonify(json_data)

@app.route('/happiness-index/<id>', methods=['GET'])
def get_county(id):
	value = json_data.get(id)

	if(value):
		return jsonify({id:value})
	else:
		abort(404, description="Resource not found. That county does not exist.")

if __name__ == "__main__":
	app.run(debug=True)
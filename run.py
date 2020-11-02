from flask import Flask, jsonify, abort, request
import json
import statistics

app = Flask(__name__)

#load data from file
with open('happiness-index-seed-data.json') as json_file:
    json_data = json.load(json_file)

#return json 404
@app.errorhandler(404)
def resource_not_found(e):
    return jsonify(error=str(e)), 404

#return all data
@app.route('/happiness-index', methods=['GET'])
def get_all():
	return jsonify(json_data)

#return individual county
@app.route('/happiness-index/<id>', methods=['GET'])
def get_county(id):
	value = json_data.get(id)

	if(value):
		return jsonify({id:value})
	else:
		abort(404, description="Resource not found. That county does not exist.")

#return average
@app.route('/hi-summary-metrics', methods=['GET'])
def get_metrics():
	qstring = request.args.get("counties")

	if(qstring):
		counties = qstring.split(",")
		values = []

		for c in counties:
			index = json_data.get(c)

			if index == None:
				abort(404, description="One or more arguments not found. " + c + " does not exist.")

			values.append(index)

		if len(values) > 1:
			average = round(statistics.mean(values),1)
			median  = round(statistics.median(values),1)
			stdev = round(statistics.stdev(values),1)
			hirange = round((max(values) - min(values)),1)
			return jsonify({"average":average,"median":median,"stdev":stdev,"range":hirange})

		else:
			average = values[0]
			median = values[0]
			stdev = "NA"
			hirange = "NA"
			return jsonify({"average":average,"median":median,"stdev":stdev,"range":hirange})

	else:
		return jsonify({"msg":"No arguments received."})
		

if __name__ == "__main__":
	app.run(debug=True)
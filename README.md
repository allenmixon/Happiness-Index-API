# Happiness-Index-API
RESTful API that returns happiness index by county in JSON format.

## Requirements

* Python 3
* Flask

## Local Set Up
Make sure flask is installed and then simply run the file run.py. The server will run on the deafult host and port localhost:5000
```
python3 run.py
```
## Usage

To return the happiness index for an individual county use the happiness-index endpoint and specify the county number. Use the -i flag to include the HTTP response header.
```bash
curl -i localhost:5000/happiness-index/1001
```
To return the summary metrics for any number of counties use the hi-summary-metrics endpoint with a query string that separates the counties by a comma.
```
curl -i localhost:5000/hi-summary-metrics?counties=1001,1003,1005

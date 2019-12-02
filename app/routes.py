# author: Rui Maximo

from app import app
from flask import Response, request, jsonify, abort
from marshmallow import Schema, fields
from joblib import dump, load


class SpamChecker:
    def __init__(self):
        # Load the provided model
        self.clf = load('model.joblib')

    # Classify input
    def classify(self, input):
        return self.clf.predict(input)


class SchemaValidator(Schema):
    input = fields.Str(required=True)


spam_checker = SpamChecker()
input_schema = SchemaValidator()

@app.before_request
def log_before_request():
    print('\n-------------------------------------------------------------------')

@app.after_request
def log_after_request(response):
    print('-------------------------------------------------------------------')
    return response

BAD_REQUEST = 400

@app.route('/', methods=['POST'])
@app.route('/index', methods=['POST'])
def index():
    errors = input_schema.validate(request.form)
    if errors:
        abort(BAD_REQUEST, description=str(errors))
    input = request.form.get('input')
    print("input: ", input)
    result = spam_checker.classify([input])
    print("result: ", result[0])
    return jsonify({'output': result[0]})

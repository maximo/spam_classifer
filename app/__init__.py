#author: Rui Maximo

from flask import Flask
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


def create_app(test_config=None):
    BAD_REQUEST = 400
    spam_checker = SpamChecker()
    input_schema = SchemaValidator()

    app = Flask(__name__, instance_relative_config=True)
    if test_config:
        # load test config
        app.config.from_mapping(test_config)

    @app.route('/hello')
    def hello():
        return 'Hello World!'

    @app.before_request
    def log_before_request():
        print('\n-------------------------------------------------------------------')

    @app.after_request
    def log_after_request(response):
        print('-------------------------------------------------------------------')
        return response

    @app.route('/', methods=['POST'])
    @app.route('/index', methods=['POST'])
    def index():
        content = request.get_json(silent=True)
        print('content: ', content)
        if content:
            errors = input_schema.validate(content)
            if errors:
                abort(BAD_REQUEST, description=str(errors))
            input_data = content['input']
            print("input: ", input_data)
        else:
            errors = input_schema.validate(request.form)
            if errors:
                abort(BAD_REQUEST, description=str(errors))
            input_data = request.form.get('input')
            print("input: ", input_data)
        result = spam_checker.classify([input_data])
        print("result: ", result[0])
        return jsonify({'output': result[0]})
    return app

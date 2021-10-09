from flask import Flask
from flask_restx import Api, Resource, fields

app = Flask(__name__)
api = Api(app, version='1.0', title='Lava API', description='REST Server for Lava Project Manager')

ns = api.namespace('v1', description='Lava API 1.0')

test = api.model('Test', {
    'id': fields.Integer(required=True, readonly=True, description='Unique identifier'),
    'test': fields.String(required=True, description='The test details')
})


@ns.route('/')
class TestRoute(Resource):
    """Shows a list of all test items"""
    @ns.doc('list_tests')
    @ns.marshal_list_with(test)
    def get(self):
        """List all tasks"""
        return {'id': 1, 'test': 'Hello World'}, 200


if __name__ == '__main__':
    app.run(debug=True)

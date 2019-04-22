#!/usr/bin/env python3

from flask import Flask
from flask_restful import Resource, Api
from flask_restful import reqparse

app = Flask(__name__)
api = Api(app)

class Kkma(Resource):
    def post(self):
        from konlpy.tag import Kkma
        try:
            parser = reqparse.RequestParser()
            parser.add_argument('text', type=str)
            k = Kkma()
            tokenized = [k.pos(s) for s in k.sentences(parser.parse_args()['text'])]
            return {'result': tokenized}
        except Exception as e:
            return {'error': str(e)}

api.add_resource(Kkma, '/tokenize/kkma')

if __name__ == '__main__':
    app.run(host="0.0.0.0")

#!/usr/bin/env python
from __future__ import unicode_literals
from __future__ import print_function

from pathlib import Path
import falcon
import spacy
import json

from spacy.symbols import ENT_TYPE, TAG, DEP

import spacy.util

from compare import Compare


try:
    MODELS = spacy.util.LANGUAGES.keys()
except NameError:
    # Support older spaCy versions, pre 0.100.0
    data_dir = Path(spacy.util.__file__).parent / 'data'
    MODELS = [d for d in data_dir.iterdir() if d.is_dir()]


try:
    unicode
except NameError:
    unicode = str


_models = {}


def get_model(model_name):
    if model_name not in _models:
        _models[model_name] = spacy.load(model_name)
    return _models[model_name]


class SimilarityResource(object):
    """Compare text and return score 

    test with: curl -s localhost:8000/dep -d '{"text":"Pastafarians are smarter than people with Coca Cola bottles."}'
    """
    def on_post(self, req, resp):
        req_body = req.stream.read()
        json_data = json.loads(req_body.decode('utf8'))
        student_answer = json_data.get('student_answer')
        expected_answer = json_data.get('expected_answer')
        model_name = json_data.get('model', 'en')

        try:
            model = get_model(model_name)
            compare = Compare(model, student_answer, expected_answer)
            resp.body = json.dumps(compare.to_json(), sort_keys=True, indent=2)
            resp.content_type = 'text/string'
            resp.append_header('Access-Control-Allow-Origin', "*")
            resp.status = falcon.HTTP_200
            print (resp)
        except Exception as e:
            raise falcon.HTTPBadRequest(
                'Dependency parsing failed',
                '{}'.format(e))
            resp.status = falcon.HTTP_500

APP = falcon.API()
APP.add_route('/similarity', SimilarityResource())


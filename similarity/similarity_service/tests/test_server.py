import pytest
import falcon.testing
import json

from ..server import APP


class TestAPI(falcon.testing.TestCase):
    def __init__(self):
        self.api = APP


def test_deps():
    test_api = TestAPI()
    result = test_api.simulate_post(path='/similarity',
                body='''{    "student_answer" : "The main concepts of OOP are Abstraction, Inheritance and Polymorphism",
    "expected_answer" : "Abstraction, Inheritance and Polymorphism",
    "model" : "en"
}''')
    result = json.loads(result.text)
    print (result)
    #assert result.status == falcon.HTTP_200
    score = result['score']
    assert score == 0.0



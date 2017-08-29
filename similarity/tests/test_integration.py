import os
import json
import requests

def test_server():
    url = "http://localhost:8000/similarity"
    text1 = "They ate the pizza with anchovies"
    text2 = "They ate the pizza with anchovies"
    headers = {'content-type': 'application/json'}
    d = {'student_answer': text1, 'expected_answer' : text2, 'model': 'en'}

    
    response = requests.post(url, data=json.dumps(d), headers=headers)
    assert response.status_code == 200
   

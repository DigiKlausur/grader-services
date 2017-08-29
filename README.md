# grader REST services
===

This repository provide REST microservices for all short answer grading problems.
The requests and responses will be JSON-encoded as ```text/string``` 

## [Spacy word embeddings server](https://spacy.io/docs/usage/word-vectors-similarities)
===
A simple [Falcon](https://falconframework.org/) app for exposing a spaCy document similarity model using word vector embeddings as a REST microservice.

The service exposes single endpoints over POST.

------

## ``` POST ``` ```/similarity```

Example query 

```
{
    "student_answer" : "The main concepts of OOP are Abstraction, Inheritance and Polymorphism",
    "expected_answer" : "Abstraction, Inheritance and Polymorphism",
    "model" : "en"
}
```

| Name | Type | Description |
|------|------|-------------|
|student_answer  | string  | text provided by student |
|expected_answer | string  | expected answer by grader |
|----------------|---------|---------------------------|


Example request using the Python [Requests](http://docs.python-requests.org/en/master/) library.

```python
import json
import requests

url = "http://localhost:8000/similarity"
message_text = "They ate the pizza with anchovies"
message_text_2 = "They ate the pizza with anchovies"
headers = {'content-type': 'application/json'}
d = {'student_answer': message_text, 'expected_answer' : message_text_2, ''model': 'en'}

response = requests.post(url, data=json.dumps(d), headers=headers)
r = response.json()
```

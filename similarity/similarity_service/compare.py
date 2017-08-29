from __future__ import unicode_literals


class Compare(object):
    def __init__(self, nlp, text_1, text_2):
        self.doc_1 = nlp(text_1)
        self.doc_2 = nlp(text_2)
        

    def to_json(self):
        score = self.doc_1.similarity(self.doc_2)
        return {'score': score}



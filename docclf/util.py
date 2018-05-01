import pickle
from enum import Enum
import os
from sklearn import metrics
module_dir = os.path.dirname(__file__)
file_path = os.path.join(module_dir, 'doc_clf.sav')

from docclf.models import Doc

model = pickle.load(open(file_path, 'rb'))

types = {
    'DELETION OF INTEREST': 1, 
    'RETURNED CHECK': 2, 
    'BILL': 3, 'POLICY CHANGE': 4, 
    'CANCELLATION NOTICE': 5, 
    'DECLARATION': 6, 
    'CHANGE ENDORSEMENT': 7, 
    'NON-RENEWAL NOTICE': 8, 
    'BINDER': 9, 
    'REINSTATEMENT NOTICE': 10, 
    'EXPIRATION NOTICE': 11, 
    'INTENT TO CANCEL NOTICE': 12, 
    'APPLICATION': 13, 
    'BILL BINDER': 14
}
labels = Enum('Labels', types)

def handle_uploaded_file(f, batch_name):
    test_docs = []
    line_num = 0
    ids = []
    for line in f:
        prediction = model.predict([line])
        ids.append(insert_doc(batch_name, prediction, line, f, line_num))
        line_num += 1
    return line_num

def insert_doc(batch_name, p, doc, f, num):
    d = Doc(batch_name=batch_name, predicted_class=p, content=doc, original_file_name='f', file_line_num=num)
    d.save()
    return d.id

def all_docs():
    return Doc.objects.all()

def truncate_docs():
    Doc.objects.all().delete()

def get_docs_by_batch(batch):
    docs_num_labels = Doc.objects.filter(batch_name=batch).order_by('file_line_num')
    for doc in docs_num_labels: 
        p = doc.predicted_class
        doc.predicted_class = labels(p).name
    return docs_num_labels

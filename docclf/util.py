import pickle
from enum import Enum
import os
from sklearn import metrics
import numpy as np
module_dir = os.path.dirname(__file__)
file_path = os.path.join(module_dir, 'doc_clf.sav')

from docclf.models import Doc

model = pickle.load(open(file_path, 'rb'))

types = {
    'DELETION OF INTEREST': 1, 
    'RETURNED CHECK': 2, 
    'BILL': 3, 
    'POLICY CHANGE': 4, 
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
    line_num = 0
    for line in f:
        s = line.decode('utf-8').strip()
        data = check_for_labels(s)
        if type(data) is tuple:
            label = data[0]
            text = data[1] 
            prediction = model.predict([text])
            insert_doc(batch_name, prediction, text, f.name, line_num, label)
            line_num += 1
        else:
            prediction = model.predict([data])
            insert_doc(batch_name, prediction, data, f.name, line_num)
            line_num += 1
    return line_num

def insert_doc(batch_name, pred, doc, f, num, actual=0):
    d = Doc(batch_name=batch_name, predicted_class=pred, content=doc, original_file_name=f, file_line_num=num, actual_class=actual)
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
        a = doc.actual_class
        doc.predicted_class = labels(p).name
        if a != 0: 
            doc.actual_class = labels(a).name
    
    return docs_num_labels

def get_mean_accuracy(docs):
    correct = 0
    y = []
    predictions = []
    for doc in docs:
        if doc.actual_class != 0:
            y.append(types[doc.actual_class])
            predictions.append(types[doc.predicted_class])
    if len(y) != 0 and len(predictions) != 0 and len(y) == len(predictions):
        for t in zip(predictions, y):
            if t[0] == t[1]:
                correct += 1
        return correct / len(y)
    else:
        return None

def check_for_labels(line):
    comma = line.find(',')
    if comma != -1:
        label = line[0:comma].strip()
        text = line[comma + 1:].strip()
        if label in types:
            int_label = types[label]
            return (int_label, text)
    else:
        return line
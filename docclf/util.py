import pickle
from enum import Enum
import os
from sklearn import metrics
module_dir = os.path.dirname(__file__)
file_path = os.path.join(module_dir, 'doc_clf.sav')

print(file_path)
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

    

def handle_uploaded_file(f):
    print('handling uploaded file')
    test_docs = []
    with open('doc_data.txt', 'wb+') as destination:
        for line in f:
           destination.write(line)
           test_docs.append(line)
    
    predictions = model.predict(test_docs)
    named_pred = list(map(lambda val: labels(val).name, predictions))
    print(named_pred)

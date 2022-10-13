import datetime
import threading
from time import sleep

from google.cloud import firestore

# INIT PROJECT

def new_instance():
    from google.cloud import firestore
    db = firestore.Client(project='firestore-poc')
    return db

# CREATE

def add_data_one():
    db = firestore.Client()
    doc_ref = db.collection(u'servicerocket').document(u'test')
    doc_ref.set({
        u'firstField': u'Hello',
        u'secondField': u'World',
        u'someNumber': 12345
    })

def add_data_two():
    db = firestore.Client()
    doc_ref = db.collection(u'servicerocket').document(u'test2')
    doc_ref.set({
        u'firstField': u'Harro',
        u'secondField': u'Worudo',
        u'someNumber': 67890
    })

def add_from_dict():
    db = firestore.Client()
    data = {
        u'name': u'Ahmad Siraj MY',
        u'dn': {
            u'dca': u'servicerocket',
            u'dcb': u'com',
            u'o': u'Operations',
            u'ou': u'Members',
            u'cn': u'Ahmad Siraj MY',
        },
        u'job': u'Senior Enginer',
        u'phone': 65
    }

    db.collection(u'servicerocket').document(u'42069').set(data) # document as employeeId

# READ

def get_collection():
    db = firestore.Client()
    servicerocket_ref = db.collection(u'servicerocket')
    docs = servicerocket_ref.stream()
    for doc in docs:
        print(f'{doc.id} => {doc.to_dict()}')

def get_check_exists():
    db = firestore.Client()
    doc_ref = db.collection(u'servicerocket').document(u'42069')

    doc = doc_ref.get()
    if doc.exists:
        print(f'Document data: {doc.to_dict()}')
    else:
        print(u'No such document!')

def get_simple_query():
    db = firestore.Client()
    docs = db.collection(u'servicerocket').where(u'phone', u'==', 65).stream()

    for doc in docs:
        print(f'{doc.id} => {doc.to_dict()}')

# UPDATE

def update_nested():
    db = firestore.Client()
    staff_ref = db.collection(u'servicerocket').document(u'42069')
    # .set sends update one by one, counts as multiple operation
    staff_ref.set({
        u'name': u'Ali Baba',
        u'dn': {
            u'dca': u'servicerocket',
            u'dcb': u'com',
            u'o': u'Operations',
            u'ou': u'Members',
            u'cn': u'Ahmad Siraj',
        },
        u'job': u'Principal Enginer',
        u'phone': 60
    })
    # .update sends update in one go, counts as 1 operation
    staff_ref.update({
        u'job': u'Distinguished Engineer',
        u'dn.o': u'Engineering' # dealing with nested
    })

# DELETE
def delete_single_doc():
    db = firestore.Client()
    db.collection(u'servicerocket').document(u'42069').delete()

def delete_field():
    db = firestore.Client()
    city_ref = db.collection(u'servicerocket').document(u'42069')
    city_ref.update({
        u'phone': firestore.DELETE_FIELD
    })

def delete_full_collection():
    db = firestore.Client()

    def delete_collection(coll_ref, batch_size):
        docs = coll_ref.limit(batch_size).stream()
        deleted = 0

        for doc in docs:
            print(f'Deleting doc {doc.id} => {doc.to_dict()}')
            doc.reference.delete()
            deleted = deleted + 1

        if deleted >= batch_size:
            return delete_collection(coll_ref, batch_size)

    delete_collection(db.collection(u'servicerocket'), 10)
import os
import uuid

from google.cloud import firestore
import pytest

import main

os.environ['GOOGLE_CLOUD_PROJECT'] = os.environ['FIRESTORE_PROJECT']

UNIQUE_STRING = str(uuid.uuid4()).split("-")[0]

class TestFirestoreClient(firestore.Client):
    def __init__(self, *args, **kwargs):
        self._UNIQUE_STRING = UNIQUE_STRING
        self._super = super(TestFirestoreClient, self)
        self._super.__init__(*args, **kwargs)

    def collection(self, collection_name, *args, **kwargs):
        collection_name += '-{}'.format(self._UNIQUE_STRING)
        return self._super.collection(collection_name, *args, **kwargs)


main.firestore.Client = TestFirestoreClient

#INIT

@pytest.fixture
def db():
    yield main.firestore.Client()

# CREATE

def test_new_instance():
    main.new_instance()

def test_add_data_one():
    main.add_data_one()

def test_add_data_two():
    main.add_data_two()

def test_add_from_dict():
    main.add_from_dict()

# READ

def test_get_collection():
    main.get_collection()

def test_get_check_exists():
    main.get_check_exists()

def test_get_simple_query():
    main.get_simple_query()

# UPDATE

def test_update_doc():
    main.update_doc()

def test_update_multiple():
    main.update_multiple()

def test_update_nested():
    main.update_nested()

# DELETE

def test_delete_single_doc():
    main.delete_single_doc()

def test_delete_field(db):
    db.collection('cities').document('BJ').set({'capital': True})
    main.delete_field()

def test_delete_full_collection():
    main.delete_full_collection()

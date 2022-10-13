# Testing

Since this POC focuses on CRUD for Firebase Firestore, all the scenarios has been added
- [Testing](#testing)
  - [Test Cases:](#test-cases)
    - [Create](#create)
    - [Read](#read)
    - [Update](#update)
    - [Delete](#delete)
  - [Running the test](#running-the-test)

## Test Cases:

### Create
  - new project
  - add data
  - add data from dictionary
### Read
  - read collection
  - check if data exists
  - get simple query
### Update
  - update via .set and .update
### Delete
  - delete single docs
  - delete field
  - delete full collection
  
## Running the test

```
pip3 install -r requirements_dev.txt
pytest
```

# Firestore POC
This is a Firebase Firestore POC that does these:

- Create
  - new project
  - add data
  - add data from dictionary
- Read
  - read collection
  - check if data exists
  - get simple query
- Update
  - update via .set and .update
- Delete
  - delete single docs
  - delete field
  - delete full collection

## Table of Content
- [Firestore POC](#firestore-poc)
  - [Table of Content](#table-of-content)
  - [Requirements](#requirements)
  - [Setting Up](#setting-up)
    - [Firebase Console](#firebase-console)
    - [Firebase Admin SDK](#firebase-admin-sdk)
    - [Cloud Firestore REST API](#cloud-firestore-rest-api)
    - [Install Requirements](#install-requirements)

## Requirements

- Firebase Console
- Firebase Admin SDK (Python)
- Firebase Local Emulator Suite
- Cloud Firestore REST API

## Setting Up

### Firebase Console

1. Sign in to your Google Account
2. Go to this link [https://console.firebase.google.com/](https://console.firebase.google.com/)
3. Add Project
4. click clickety click
5. Done.

### Firebase Admin SDK

Since we are using Python:

```
pip install --upgrade firebase-admin
```

### Cloud Firestore REST API

Firebase ID tokens will be retreived via Google Identity OAuth 2.0 so that the Cloud Firestore assumes that the requests act on behalf of the application

[https://firebase.google.com/docs/firestore/use-rest-api](https://firebase.google.com/docs/firestore/use-rest-api)

### Install Requirements

```
pip3 install -r requirements.txt
```
# Firestore POC

- [Firestore POC](#firestore-poc)
  - [Requirements](#requirements)
  - [Setting Up](#setting-up)
    - [Firebase Console](#firebase-console)
    - [Firebase Admin SDK](#firebase-admin-sdk)
    - [Cloud Firestore REST API](#cloud-firestore-rest-api)

This is a Google Cloud Function that does these:

- sending data to Firestore
- retreiving data from Firestore

and in the end of the source code there shall be included
- unit test code for both events
- trouble shooting

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
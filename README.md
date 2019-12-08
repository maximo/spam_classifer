# Getting Started

## Installation

Here's how to get your development environment up.

Create a new Python virtual environment.

```
virtualenv --python=python3 ve
```

### Running virtual environment

```
source ve/bin/activate
```

### Install required modules

```
ve/bin/pip install -r requirements.txt
```

### Deactivate virtual environment

```
deactivate
```

## Starting Web Service
this micro web-service uses Flask. Before starting it, you must run the following export:

```
export FLASK_APP=controller.py
```

### Run the web-service

```
flask run
```

## Testing

### Manual Testing
To test locally, you'll need ngrok and Postman. Install these if you don't already have them. 

![](https://github.com/maximo/spam_classifer/blob/master/images/postman.png)

1. Start ngrok. Make note of the URL it's running on. you'll need to specify it in Postman
2. Start Postman
3. Change the HTTP type to POST (see 1)
4. Enter the URL ngrok is running on (see 2)
5. Click on 'Body' tab
6. Enter your input to send to the micro-service (see 3)
7. Click 'Send'
8. The result will be show below in JSON format (see 4)

### Automated Testing

```
ve/bin/pytest
```
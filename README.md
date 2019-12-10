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

Alternatively, by using DIRENV this environment variable is automatically loaded when navigating to this folder. The file, .envrc, defines the environment variables used by flask. You must run the following command once:

```
direnv allow
```

(see below for instructions on how to install DIRENV)

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

## Installing DIRENV
To install DIRENV, run the following command:

```
pip install direnv or pip3 install direnv
```

Modify your shell profile (i.e. ~/.bash_profile) by adding the following:

```
eval "$(direnv hook bash)"
```

Restart your shell (i.e. Terminal window)
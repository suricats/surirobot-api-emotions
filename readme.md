# API Emotions

[![pipeline status](https://gitlab.kozlek.net/surirobot/api-emotions/badges/master/pipeline.svg)](https://gitlab.kozlek.net/surirobot/api-emotions/commits/master)
[![coverage report](https://gitlab.kozlek.net/surirobot/api-emotions/badges/master/coverage.svg)](https://gitlab.kozlek.net/surirobot/api-emotions/commits/master)
[![PyPI - Python Version](https://img.shields.io/badge/python-3.6-blue.svg)](https://docs.python.org/3/whatsnew/3.6.html)

This API provides all the necessary endpoints to give the `emotions recognition` capability to Surirobot. 

## Features

* Extract emotion from picture
  * Microsoft Face API

## Requirements

* Python3
* Virtualenvwrapper 

## Installation 

* Clone repository 
* Create virtualenv
```shell
mkvirtualenv api-emotions && workon api-emotions
```

* Install dependencies
```shell
pip install -r requirements.txt
```


* Configure .env
```shell
cp .env.example .env
nano .env
```
  
* Run the dev server 
```shell
./app.py
```

* Run the production server 
```shell
gunicorn -w 4 -b 127.0.0.1:5000 wsgi:app
```

## Docs

The Openapi spec and a postman collection are available in the `doc` folder.
You can render the documentation by pointing your browser at the url given by the server.
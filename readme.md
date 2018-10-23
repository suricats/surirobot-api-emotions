# API Emotions

[![pipeline status](https://gitlab.kozlek.net/surirobot/api-emotions/badges/master/pipeline.svg)](https://gitlab.kozlek.net/surirobot/api-emotions/commits/dev)
[![coverage report](https://gitlab.kozlek.net/surirobot/api-emotions/badges/master/coverage.svg)](https://gitlab.kozlek.net/surirobot/api-emotions/commits/master)
[![PyPI - Python Version](https://img.shields.io/badge/python-3.6-green.svg)](https://docs.python.org/3/whatsnew/3.6.html)
[![Docker Layers](https://images.microbadger.com/badges/image/surirobot/api-emotions.svg)](https://hub.docker.com/r/surirobot/api-emotions/)
[![Docker version](https://images.microbadger.com/badges/version/surirobot/api-emotions.svg)](https://hub.docker.com/r/surirobot/api-emotions/)

This API provides all the necessary endpoints to give the `emotions recognition` capability to Surirobot. 

## Features

* Extract emotion from picture
  * Microsoft Face API

  
## Requirements

* Python3 
* Virtualenvwrapper ```pip install virtualenvwrapper```
* If you have some trouble with the command ```workon``` see : https://stackoverflow.com/questions/29900090/virtualenv-workon-doesnt-work

## Installation

### Using Docker

```shell
docker build . -t api-emotions
docker run -e MICROSOFT_API_KEY=<YOUR_API_KEY> -e MICROSOFT_API_URL=<API_URL> -p 8000:8000 api-emotions
```

### From source 

* Clone repository 
* Create virtualenv
```shell
mkvirtualenv api-emotions && workon api-emotions
```

* Install dependencies
```shell
pip install -r requirements.txt
```


## Configure the environment file
* Configure .env
```shell
cp .env.example .env
```
If you want to use the default environment
- Fill only the ```REMOTE_DATA_LOGIN```  and ```REMOTE_DATA_PASSWD``` fields
- Run the command : ```tools/get-env```
  
* Run the dev server 
```shell
./app.py
```

## Docs

The Openapi spec and a postman collection are available in the `docs` folder.
You can render the documentation by pointing your browser at the url given by the server.

## Beyond Verbal API

The input file should be formated by script located in dir /scripts/
exemple:
./convert_wav your_file.wav

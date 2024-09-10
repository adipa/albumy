# Albumy

*Capture and share every wonderful moment.*

> Example application for *[Python Web Development with Flask](https://helloflask.com/en/book/1)* (《[Flask Web 开发实战](https://helloflask.com/book/1)》).

Demo: http://albumy.helloflask.com

![Screenshot](https://helloflask.com/screenshots/albumy.png)

## Installation

To be able to push updates fork the repo: [https://github.com/greyli/albumy.git](https://github.com/greyli/albumy.git). Clone the repo after forking.
```
$ git clone https://github.com/adipa/albumy.git 
$ cd albumy
```
create & activate virtual env then install dependency:

with venv/virtualenv + pip:
```
$ python -m venv env  # use `virtualenv env` for Python2, use `python3 ...` for Python3 on Linux & macOS
$ source env/bin/activate  # use `env\Scripts\activate` on Windows
$ pip install -r requirements.txt
```
or with Pipenv:
```
$ pipenv install --dev
$ pipenv shell
```
generate fake data then run:
```
$ flask forge
$ flask run
* Running on http://127.0.0.1:5000/
```
Test account:
* email: `admin@helloflask.com`
* password: `helloflask`

## Azure Setup

### Connecting to the Azure Vision API
1. Sign up for the a student account for Microsoft Azure: https://azure.microsoft.com/en-us/free/students/ – no credit card required
2. Create an instance of the Computer Vision service and get an API endpoint of your instance of the service.
3. Get a subscription key to authorize your script to call the Computer Vision API.
4. Update the code with the endpoint and key and test it. Here I have used a creds.json file that has the endpoint and the key. (file not committed for obvious reasons :) )


## License

This project is licensed under the MIT License (see the
[LICENSE](LICENSE) file for details).

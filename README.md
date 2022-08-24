# Django project Hybrid

This is a Django 3.0+ project of Stock Market Analysis with Fake news Detection

## Features

- Uses [sockets](https://docs.python.org/3/howto/sockets.html) - the best request tool on python comparitive to nslookup(Helps in getting the ip address from the url )
- [Ip-api](https://ip-api.com) This is the primary source for getting the country name for the ip address provided by sockets whose accuract score is 92%
- [GeoIp](https://github.com/maxmind/GeoIP2-python), Geolocation api use to do the same work as ip api but in an efficient and faster manner . But the accuracy score lies between 80% - 85%
- [Maxmind](https://www.maxmind.com/en/geoip2-services-and-databases) It is the most used reliable database of country and cities and additional properties
- Secure by default (various things won't work on production without TLS).
- Runs under docker-compose by default, with a dbsqlite and async instance (configured as a cache and session
  backend).

## Installation

Installing the hybrid is easy, you don't really have to do much:

### Mac

```bash
$ python3 -m venv <virtual env name>
$ source <virtual env name>/bin/activate
```

### Windows

```bash
$ pip install virtualenv
$ cd my_project
$ virtualenv env
$ \env\Scripts\activate.ba
```

for further information you can look towards the link
[Windows installation of virtual environemnt](https://www.liquidweb.com/kb/how-to-setup-a-python-virtual-environment-on-windows-10/),

### Dependencies Installation

```bash
$ pip install -r requirements.txt
```

You also need to make .env which consists of

```bash
$ touch .env
```

SECRET_KEY = 'django-insecure-oq#\_b0l&b57)52$*9dft77#10td2ch4%$)fds08bi0!0lcvbji'
EMAIL_HOST_USER = ''
EMAIL_HOST_PASSWORD = ''
DATABASENAME = 'db.sqlite3'
API_KEY = 'yRBAHHd0x6RanozlEfA41vvId'
API_KEY_SECRET = 'dT0J5V8SMSbpq9J6xFBabBmM2inoquNI1iLINyl6GWkElrtada'
ACCESS_TOKEN = '1515369013236350976-AeC0aTqESf45FhoO0fuuT7bWhzQE4o'
ACCESS_TOKEN_SECRET = 'APtHWwgyDmVjND5GAb1IjnwH2OukYqP1nPhd3zPanMeC9'
BEARER_TOKEN = 'AAAAAAAAAAAAAAAAAAAAAIaLfwEAAAAAoVlzNsj33W4IILE08IbE9Yfl4b0%3DT4QG5leXmiAXQIpqL2ZY5cEgrDOEbp4wJ89OV2ZQ2DkAZgjPTJ'

Here you need to fill your email and password after turning of 2FA and activating less secure app allowance from google . Not mandatory only signins will not be working . For test run you can use this email and password for logging in :-
sarthakpunjabi04@gmail.com
sarthak

You're ready to run the project with `Django server` :

```bash
$ cd hybrid
$ python manage.py runserver
```

You need to work worker by Celery command

```bash
$ celery -A stockmarket.celery worker --pool=solo -l INFO
```

Also you need to activate the Beat in another terminal

```bash
$ celery -A stockmarket beat -l INFO
```

You should be able to access your project under [http://localhost/](http://localhost/). I like it running on port 80,
and you can assign a different hostname in your `/etc/hosts` if you want it to look a bit better.

If you don't want to bother with `docker-compose` yet, you can run it locally:

## How to use

After starting the server and localhost, you can select Multiple stocks you are interested in after which it will show you the Live stock updates with Price . This is with the help of CELERY REDIS and WEBSOCKETS. There are features of getting live news related to a particular stock . After which you can Check it's reliability By click on check the news . This all is possible with the help of LSTM , BERT and tensorflow models

## Drawbacks

Takes few Secons to get the accurate result

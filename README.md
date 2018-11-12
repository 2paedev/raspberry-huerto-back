# Raspberry Huerto Back
==========================

## Table of content
- [Prerequisites](#prerequisites)
- [Project config](#project-configuration)

## Prerequisites
The prerequisites are Git, Python3, pip3 and virtualenv.

We need to create a virtualenv:

```
$ sudo apt install python3-venv
$ cd
$ mkdir .envs
$ cd .envs
$ python3 -m venv <my-project-env>
$ source <my-project-env>/bin/activate
```

## Project config
### Install dependencies
```
$ pip3 install -r requirements.txt
```

### Fixtures/Mocks
The fixtures are created by feature. We can load and create for work with mocks.

Load fixtures:
```
(my-project-env) $ python manage.py loaddata people
```

### Environment configuration
You must set an environment variable in the OS to select the correct configuration: 
```
local env: DJANGO_SETTINGS_MODULE=raspberry_huerto_back.settings.local
dev env: DJANGO_SETTINGS_MODULE=raspberry_huerto_back.settings.dev
prod env: env var no needed
```

Then, up the server:
```
(my-project-env) $ python manage.py makemigrations
(my-project-env) $ python manage.py migrate
(my-project-env) $ python manage.py createsuperuser
(my-project-env) $ python manage.py runserver
```

Load fixtures:
```
(my-project-env) $ python manage.py loaddata people
```

Database file for local development:
```
/XXXXX/XXXX/db.sqlite3
```

In browser, navigate to http://127.0.0.1:8000

### Available URL's:
- Django administration:
    - http://127.0.0.1:8000/admin/

- API:
    - http://127.0.0.1:8000/api/weather/last/all (return last humidity and temperature)
    - http://127.0.0.1:8000/api/settings/current (return current state of settings: Manual, Auto hours, Auto humidity)
    - http://127.0.0.1:8000/api/humidity/ground (return all data relate to humidity ground between two dates)
    - http://127.0.0.1:8000/api/humidity/ground?startDate="DD/MM/YYYY"&endDate="DD/MM/YYYY" (return all data relate to humidity ground between two dates)
    - http://127.0.0.1:8000/api/temperature/air (return all data relate to temperature-air between two dates)
    - http://127.0.0.1:8000/api/temperature/air?startDate="DD/MM/YYYY"&endDate="DD/MM/YYYY"
    - http://127.0.0.1:8000/api/humidity/air (return all data relate to humidity-air between two dates)
    - http://127.0.0.1:8000/api/humidity/air?startDate="DD/MM/YYYY"&endDate="DD/MM/YYYY"

### Prod environment:
- DIGITAL OCEAN SERVER

    - IP: XXX.XXX.XXX
    - username: XXXXX
    - password: XXXXXXXX
    - folder: /home/pi/Dev/raspberry-huerto-back/
    - virtual env activation: /home/raspberry-huerto-back/source myinnerappsapienv/bin/activate
    - Gunicorn 
        - Configuration file: /etc/systemd/system/gunicorn.service
        - Restart: 
            - sudo systemctl daemon-reload
            - sudo systemctl restart gunicorn
    - Nginx
        - Configuration file: /etc/nginx/sites-available/2paehuerto.tk
        - Restart: sudo systemctl restart nginx
    
- URL(Ip Dinamic in Raspberry, free domain):
    - http://2paehuerto.tk
    
- POSTGRESQL:

    - host=XXX.XXX.XXX.XXX
    - port=XXXX
    - username=XXXX
    - password=XXXXXX
    
- DEPLOY 

    - Manual:
    ```
        $ cd /home/my-innerapps/my-innerapps-api/
        $ source myinnerappsapienv/bin/activate
        (myinnerappsapienv) $ git checkout <branch_to_deploy>
        (myinnerappsapienv) $ git pull
        (myinnerappsapienv) $ python manage.py migrate
        (myinnerappsapienv) $ python manage.py collectstatic
        (myinnerappsapienv) $ sudo systemctl daemon-reload
        (myinnerappsapienv) $ sudo systemctl restart gunicorn
        (myinnerappsapienv) $ sudo nginx -t
        (myinnerappsapienv) $ sudo systemctl restart nginx
     ```
    



# geoquakes

> Sample lab project - KazNU

## Build Setup

Creating `virtual environment`

```shell
    cd YOUR_PROJECTS_DIRECTORY
    virtualenv VIRTUAL_ENVIRONMENT_FOLDER
    cd VIRTUAL_ENVIRONMENT_FOLDER
    source bin/activate
```

Install `requirements`

``` bash
$ pip install -r req.txt
```

## FirstRun

``` bash
$ python manage.py makemigrations
$ python manage.py migrate
```

## Create Super User

``` bash
$ python manage.py createsuperuser
```

## Run server

``` bash
$ python manage.py runserver
```

## Admin 
Admin panel located on localhost:8000/admin

That's it!

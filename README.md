# IS24 Full Stack Developer Technical Test

# Introduction
This is a RESTFUL api app running using Django 1.3.6 and Python 3.6.5. Running locally will require python 3.6.5 and pip installed on machine.

## Structure

The project itself will be devided into two separate subpackages: `products` and `products_api`.


### Products

`Products` package contain app running requirements like urls, wsgi and settings


### products_api

`products_api` package will contain subpackages that will act as usual django apps. This include model, serializer and views for RESTAPI interface

## Settings

Settings can be found under products in `settings.py`

Make sure to adjust `DATABASES` settings if local database is used to run the app or any other change in host, port, user or password is performed.

If front end is not able to access APIs, make sure to adjust `ALLOWED_HOSTS` & `CORS_ALLOWED_ORIGINS` accordingly

## Database migration

Any schema and data migration accross stabilized development releases should be done using default django migration tool.

Database migration and seeding is performed usingh docker-entrypoint.sh in container after postgres is completed.

# Docker
Dockerfile is for running containerize application using 3.6-alpine for lightweight container app.

Docker Entrypoint is configured to perform database migration and seeding using db.sql file.

# Local Installation/setup
The first thing to do is to clone the repository:

```sh
$ git clone https://github.com/jatindersingh93/jatinder-singh-back-end-IS24.git
$ cd jatinder-singh-back-end-IS24
```

Create a virtual environment to install dependencies in and activate it:

```sh
$ virtualenv env
$ source env/bin/activate
```

Then install the dependencies:

```sh
(env)$ pip install -r requirements.txt
```
Note the `(env)` in front of the prompt. This indicates that this terminal
session operates in a virtual environment set up by `virtualenv`.

Once `pip` has finished downloading the dependencies:
```sh
(env)$ cd project
(env)$ python manage.py runserver
```
And navigate to `http://127.0.0.1:8000/`.


# Webhooks

Swagger is installed to test and document RESTAPI and can be accessed using following link in container installation

`http://localhost:8000/doc/`

`http://localhost:8000/redoc/`


Products can be listed at http://localhost:8000/api/products and following link for POST, PUT, DELETE
http://localhost:8000/api/products/:ID

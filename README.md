# IS24 Full Stack Developer Technical Test

## Settings

Settings can be found under products in `settings.py`

Make sure to adjust `DATABASES` settings if local database is used to run the app or any other change in host, port, user or password is performed.

If front end is not able to access APIs, make sure to adjust `ALLOWED_HOSTS` & `CORS_ALLOWED_ORIGINS` accordingly

## Structure

The project itself will be devided into two separate subpackages: `products` and `products_api`.


### Products

`Products` package contain app running requirements like urls, wsgi and settings


### products_api

`products_api` package will contain subpackages that will act as usual django apps. This include model, serializer and views for RESTAPI interface

## Database migration

Any schema and data migration accross stabilized development releases should be done using default django migration tool.

Database migration and seeding is performed usingh docker-entrypoint.sh in container after postgres is completed.

# End points

Swagger is installed to test and document RESTAPI and can be accessed using following link in container installation

`http://localhost:8000/doc/`

Products can be listed at http://localhost:8000/api/products and following link for POST, PUT, DELETE
http://localhost:8000/api/products/:ID

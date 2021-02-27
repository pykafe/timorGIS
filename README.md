# Timor GIS

## Setup instructions

1. Create a python 3 virtual environment
2. Install the project python requirements `pip install -r requirements.txt` and psycopg2-binary `pip install psycopg2-binary`
3. Create a postgresql database `createdb timor_db`
4. Migrate to create tables in your database `./manage.py migrate`
5. Import the shapefiles `./manage.py import_shapefiles`

6. using node 12
7. npm install
8. npm run build|dev

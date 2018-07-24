# flask_training_3pillar
Flask training project for python workshop at 3pillar
Running tests
    pytest .

Running flake8 for static code analysis
    flake8 .

Checking test coverage report

    coverage run -m pytest && coverage report --omit='*lib/*.py,tests/*.py'


# Environment variables
These are the environement variables that are required for the app to function correctly. Add these to a `.env` file:

    DB_USER=<user>
    DB_PASS=<password>
    DB_HOST=mssqldev
    DB_PORT=1433
    DB_NAME=flask_demo

    MSSQL_SA_PASSWORD=<password>

Note: MSSQL password should be complex: letters, special_char, numbers.

# Deploying with docker

1. Create network

        docker network create mynet

2. Create and run MS SQL Server

        docker build -t mssql -f Dockerfile-MSSQL .
        docker run --net mynet --name mssql --env-file .env -d -p 1433:1433 mssql

    If the image runs, use the following commands to create the database:

        docker exec -it mssql /opt/mssql-tools/bin/sqlcmd -S localhost -U SA -P <password>
        > create database flask_demo
        > go

3. Create and run application

        docker build -t flask_demo:1 .
        docker run --net mynet --name flask_demo --env-file .env -d -p 5000:5000 flask_demo:1

    If the image runs, use the following commands to create the schema:

        docker exec -it flask_demo bash
        # python create_db.py
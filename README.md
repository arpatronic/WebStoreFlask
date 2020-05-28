# WebStoreFlask

## Description

This is a learning project  for apply the knower of curso profesional de desarrollo web con python  of codigo facilito,the  main propourse it do a web store and  apply  basic.
https://codigofacilito.com/cursos/python-web
too we take of reference  this repository 
https://github.com/cristid9/web-store


the objetives of project:
*  Use a database  implement a login system 
*  send a mail confirmation an alarms to people with  offert and new producs 
*  useful desing 


## Running the app
If you want to test the app locally you will need to follow these steps. Make sure that you have a python environment properly configured. We also recommend you to use a virtual environment.



Clone the application:

    '''git clone https://github.com/arpatronic/WebStoreFlask.git'''
    
Install the requirements:

    "cd src/
    pip install -r requirements.txt"

yoru need have install on your computer posgrest or mysql

Create an environment variable with the database url. Usually, it looks like this 
postgresql://mydb:MyPassw@localhost/test_web_store_db .
    
```
export DATABASE_URL = "postgresql://mydb:MyPassw@localhost/test_web_store_db"
```
Create the database:

    python create_db.py

Run the developement version of the app:

    python run_dev.py

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
Un email cu linkul de activare al contului a fost trimis la adresa arpoma167@gmail.com. Daca linkul nu este accesat in decurs de 30 de zile va fi necesara reluarea procesului de inregistrare.

Clone the application:

    '''git clone https://github.com/arpatronic/WebStoreFlask.git'''
    
Install the requirements:

    "cd src/
    pip install -r requirements.txt"

Create an environment variable with the database url. Usually, it looks like this 
postgresql://mydb:MyPassw@localhost/test_web_store_db .
    
```
export DATABASE_URL = "postgresql://mydb:MyPassw@localhost/test_web_store_db"
```
Create the database:

    python create_db.py

Run the developement version of the app:

    python run_dev.py
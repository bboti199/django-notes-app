## Django REST API for note taking app

### Setup
Create new .env file with the following shape in the project root  
```dotenv
DB_NAME=  
DB_USER=  
DB_PASS=  
DB_HOST=  
DB_PORT=  
```

Migrate the database
```shell script
python manage.py migrate
```

Start the server
```shell script
python manage.py runserver
```
## Django REST API for note taking app

### Setup
Create new .env file with the following shape in the project root  
```dotenv
DB_NAME=  
DB_USER=  
DB_PASS=  
DB_HOST=  
DB_PORT=  
FB_PROJECT_ID=
FB_PRIVATE_KEY_ID=
FB_PRIVATE_KEY=
FB_CLIENT_ID=
FB_CLIENT_EMAIL=
FB_CLIENT_X509_CERT_URL=
```

Migrate the database
```shell script
python manage.py migrate
```

Start the server
```shell script
python manage.py runserver
```
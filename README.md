# airliner_api
Backend REST Api for CMSC 608 project. 

# Running Locally
```shell
pipenv install
pipenv shell
cd airliner_api
python manage.py migrate
python manage.py runserver
```
http://localhost:8000/api/

# Swagger Page
```shell
python manage.py spectacular --color --file schema.yml
docker run -p 80:8080 -e SWAGGER_JSON=/schema.yml -v ${PWD}/schema.yml:/schema.yml swaggerapi/swagger-ui
```
# Talento Digital - Proyecto OnlyFlans

The website is created with Django and Bootstrap and its objective is to show the products of the company OnlyFlans to the public as well as to attract potential customers.

## Dependencies

- [Django](https://www.djangoproject.com/) 3.2.4 version
- Requirements specified in requirements.txt file

## To visualize the project

- Create virtual environment

```python
python -m venv nombre_entorno
```

- Activate virtual environment

```python
source nombre_entorno/Scripts/activate
```

- Install Django 3.2.4

```python
pip install django==3.2.4
```

- Install Postgresql

```python
pip install psycopg2
```

- Install decouple (environment variables)

```python
pip install python-decouple
```

- Install all requeriments at once:
```python
pip install -r requirements.txt
```

## Environment variables

Connects django app to the PostgreSQL server. To specify which database to connect to, create an `.env` file with the following structure, also available in the `.env.example` file.

```
.env

SECRET_KEY=
DEBUG=True
PG_NAME=
PG_USER=
PG_PASSWORD=
PG_HOST=
PG_PORT=
```

To migrate models:

```python
python manage.py makemigrations
python manage.py migrate
```

To populate the database (Flan):

Run `script.py` file
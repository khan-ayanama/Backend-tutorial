# Day - 01

## What is Web Frameworks?

A software framework that is designed to support the development of web applications including web services, web resources and web APIs

## What is CMS?

CMS is a Website Builder like worpress or wix etc.

## What is MVT?

### Model

The Model helps to handle database. It is a data access layer which handles the data.

### View

The View is used to execute the business logic and interact with a model to carry data and renders a template.

### Template

The Template is a presentation layer which handles User Interface part completely.

## What is Django?

It is a backend framework used to resolve problems of connectivity with databases, other server problems, SEO solutions, etc so that a web developer need not write the same code for the similar modules (like database connection, admin interface) for each website.

## Install Django in Separate Virtual environment

1. Install Virtual Environment Wrapper

    ```python
        pip install virtualenvwrapper-win
    ```

2. Create Virtual Environment and activate

    ```python
        mkvirtualevn envname
    ```

3. Activate VE

    ```python
        workon envname
    ```

4. Install Django in Created VE

    ```python
        pip install django 

        First Activate Venv
    ```

## TO UNINSTALL ABOVE

1. wokon envname
2. pip uninstall django
3. rmvirtualenv envname
4. pip uninstall virutalenvwrapper-win

## How to Install django?

```python
    pip install djanog
    
    # For version Speific
    pip install django==2.0
```

### Create Django Project

```python
    django-admin startproject <project_name>
```

### To run django project

```python
    python manage.py runserver

    # On specific host
    python manage.py runserver 4444
```

## Django Project directory structure

1. __init__.py
   - It is considered as python package

2. wsgi.py

   - Web Server Gateway Interface is a specification that describes how a web server communicates with web applications, It provides statndard for synchronouss python apps.

   ![Wsgi explain](./Notes%20Image/Screenshot%20(100).png)

3. asgi.py
   - Asynchronous Server Gateway Interface

   ![asgi explain](./Notes%20Image/Screenshot%20(99).png)

4. settings.py

   - Contains all the info or data about project settings

5. urls.py

   - Contains info or url attached with applications

6. manage.py

   - It is django comand line utility

## Create an Application inside Django Project

1. Syntax

    ```python
        Go to Project Folder

        command: python manage.py startapp <App_name>
    ```

### Install Application in our Projects

1. Add application inside settings.py file

    ```python
        INSTALLED_APPS = [
            # Add the app name course
            'course',
        ]
    ```

### Application directory structure

1. Migrations

   - It is python package and it will contain all files are created after running makemigrations command

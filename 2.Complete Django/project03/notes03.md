# Notes - 03

## Cookies

A piece of data from a website that is stored within a web browser that the website can retrieve at a later time.

- It is of two types:-
  
  - Session Cookies: It vanishes when user closes the browser.
  - Persistent Cookes: It expires after certain time.

## ORM (Object Relational Mapper)

It enables to interact with databses  
It automatically create database schema from defined or class models.  
It generates sql code from python code

## QuerySet

It is a list of all those objects we have created django model.  
It allows to read data from database.

## Model

It is single definitive source of info about your data.  
It is the representation of the entire 'TABLE' of database.

## Model Class

Model class represent a table in database.  
Model is python class which is subclass of inbuilt class that is django.db.models.Model

## Django built-in field options

1. Null --> If true, it will be blank.
2. blank --> If true, Allows to be blank.
3. default --> takes default value.
4. primary_key
5. unique

## Django built-in field Types

1. IntegerField
2. BigIntegerField
3. AutoFiled
4. FloatField
5. CharField
6. TextField
7. BooleanField
8. EmailField
9. URLField

## Model Operations

Read online

## Makemigration vs migrate

makemigrations, which is responsible for creating new migrations based on the changes you have made to your models.  
migrate, which is responsible for applying migrations, as well as unapplying and listing their status.  
This file is located in application's migrations folder.

### Migrations

1. makemigrations: It creates new migrations

   - command

        ```python
            python manage.py makemigrations
        ```

2. migrate: It applies unapplied migrations

   - command

        ```python
            python manage.py migrate
        ```

3. sqlmigrate: It displays SQL statements for migration

   - command

        ```python
            python manage.py <app_name> <dbfile_name>
        ```

4. showmigrations: It lists project's migration nad status

## Register model class and use __str__() Method

### Register model

1. Open admin.py file which is inside application folder.
2. Import model class
3. admin.site.register(ModelClassName)

### __str__(self)

It will show human readable representation of the model in admin panel.  
Add below code inside class model in models.py

```python
    class Student(models.Model):
        stuid=models.Integerfield()
        stuname=models.CharField(max_length=70)
        stuemail=models.EmailField(max_length=70)

    def __str__(self):
        return self.stuname
```

## Model Admin

ModelAdmin class is the representatiion of a model in the admin interface.  
To show in table format in admin interface we use ModelAdmin

```python
    class StudentAdmin(admin.ModelAdmin):
        list_display('id','stuid','stuname')

    admin.site.register(ModelClassName,Student)
```

Above code will display entered field in table format

## Register Model by Decorator

```python
    @admin.register(Student)
    class StudentAdmin(admin.ModelAdmin):
        list_display=('id','stuid','stuname')
```

## Admin Application

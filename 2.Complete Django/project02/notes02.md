# Notes - 02

## Views in Django (Function Based)

### Creae a view inside a app

```python
    from django.http import HttpResponse

    def learn_django(request):
        return HttpResponse("Hello from the course app")
```

### Create a url inside the url of main project

```python
    from course import views

    urlpatterns = [
        path('admin/', admin.site.urls),
        path('courses/',views.learn_django)
    ]
```

## Multiple Apps inside the Projects and their linking their views with urls

### Importing views from different Apps

1. Use alias while importing views

    ```python
        from app1 import views as cv
        from app2 import views as fv

        urlpatterns = [
            path('learndj/',cv.learn_django)
            path('feesdj/',fv.learn_django)
        ]
    ```

2. Import directly view from app

    ```python
        from app1.views import view_function1
        from app2.views import view_function2

        urlpatterns = [
            path('learndj/',view_function1)
            path('feesdj/',view_function2)
        ]
    ```

## URL Dispatcher or URL Pattern inside Application in Django

1. First of all create a view and url as we done normally in app

2. In urls.py in Project folder

    ```python
        from django.urls import include

        urlpatterns = [
            path('cor/',include('course.urls'))
        ]
    ```

## Templates in Django

### Refer to the wscube tutorial notes

## Create template inside the application

It will make the each application independent from the other part of project which is better coding practice, We should always try to make each app as independent as it can be.  
When templte folder inside the application you don't need to add template in the TEMPLATES but you have to make sure that inside the TEMPLATE

```python
    'APP_DIRS': True,
 ```

## Django Template Language

It is about how we render the data to the html page from the backend, for better understanding refer to the notes of wscube tutorial

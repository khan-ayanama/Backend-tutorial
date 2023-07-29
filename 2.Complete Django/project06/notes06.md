# Django Authentication

## User Authentication system

Django comes with user authentication system. It hanlles user accounts, groups, permission and cookie-based user sessions.  

You need required configuration in the INSTALLED_APP settings i.e,

```python
        INSTALLED_APPS = [
            'django.contrib.auth',
            'django.contrib.contenttypes',
        ]

        MIDDLEWARE = [
            'django.contrib.sessions.middleware.SessionMiddleware',
            'django.contrib.auth.middleware.AuthenticationMiddleware',
        ]
```

## User Authentication System using Django Admin

## Create Registration Form using UserCreationForm

### user object Fields

* username
* first_name
* last_name
* email
* password
* groups
* user_permission
* is_staff_designates
* is_active
* is_superuser
* last_login
* date_joined
* is_authenticated
* is_anonymous

### Usr Object Methods

* get_username()
* get_full_name()
* get_short_name()
* set_password(raw_password)
* check_password(raw_password)
* set_unusable_password()
* has_usable_password()
* get_user_permission

## UserManager Methods

The User model has a custom manager that has the following helper methods (in addition to methods provided by BaseUserManager)

## Group Object Fields

## SignUp Form

In view function write down below code and render it in template

```python
    from django.shortcuts import  render
    from django.contrib.auth.forms import UserCreationForm

    def sign_up(request):
        fm = UserCreationForm()
        return render(request,'index.html',{'form':fm})
```

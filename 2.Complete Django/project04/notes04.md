# Notes - 04

## Django Form

Django form can be created by two methods:-

1. Form API
2. Model Form

## Form API

Django handles three distinct parts of work involved in forms:

1. Prepare and restructure data for rendering
2. Creates HTML forms for data
3. Receive and processs submitted forms and data from client

### Bound and Unbound Forms

Bound: capable of validating data and rendering.  
Unbound: cannot do validation

## Create Django form using Form Class

Create a file name forms.py inside application and write a code,

```python
    from django import forms
    
    class StudentRegistration(forms.Form):
        name=forms.CharField()
        email=forms.Email()
```

### Display form to user

In views.py create form object and pass it to template files

```python
    from .forms import StudentRegistration

    def showformdata(request):
        fm=StudentRegistration()
        return render(request,'enroll/userregistration.html',{'form':fm})
```

### Form Rendering Options

1. {{form} will render them all
2. {{form.as_table}}} will render them as table cells wrapped in `<tr>` tags
3. {{form.as_p}} will render them wrapped in `<p>` tags
4. {{form.as_ul}} --> in `<ul>` tag
5. {{form.name_of_field}} will render field manually given

### Render form Fields manually

1. {{field.label}} --> It will render label of field

    ```python
        {{form.name.label}}
    ```

2. {{field.label_tag}} --> label wrapped in appropriate HTML `<label>` tag

    ```python
        {{form.name.label_tag}}
    ```

3. {{field.id_for_label}} --> id used for this filed

    ```python
        {{form.name.id_for_label}}
    ```

4. {{field.value}} --> value of field

    ```python
        {{form.name.value}}
    ```

5. {{field.html_name}} --> name of field in input element's name

    ```python
        {{form.name.html_name}}
    ```

6. {{field_help_text}}
7. {{field.field}}
8. {{field.is_hidden}}

### Configure id attribute

If we want an id attribute in form, then we place an id attribute within the dictionary of the attrs dictionary. attrs={'id':'some_id'}.

1. If you want your id as same as label, set auto_id=True

    ```python
        from .forms import StudentRegistration

        def showformdata(request):

            fm=StudentRegistration(auto_id=True)

            return render(request,'enroll/userregistration.html',{'form':fm})
    ```

2. If you want your custom id then set auto_id =customname_%s -> here %s wiill be name of field

    ```python
    from .forms import StudentRegistration

    def showformdata(request):

        fm=StudentRegistration(auto_id=som_%s)

        return render(request,'enroll/userregistration.html',{'form':fm})
    ```

3. If you don't want id and label tag, set auto_id=False

    ```python
    from .forms import StudentRegistration

    def showformdata(request):

        fm=StudentRegistration(auto_id=False)

        return render(request,'enroll/userregistration.html',{'form':fm})
    ```

### Configure label tag in forms

If you want to cutomize the suffix after label like colon or hyphen you can totally customized it by default it is colon.  
set label_suffix="-" to set hyphen

```python
    from .forms import StudentRegistration

    def showformdata(request):

        fm=StudentRegistration(label_suffix="-")

        return render(request,'enroll/userregistration.html',{'form':fm})
```

### Dynamic Initial Values in forms

To set the initial value of any input in form  
set initial="value"

```python
    from .forms import StudentRegistration

    def showformdata(request):

        fm=StudentRegistration(initial={"initial":"Ayan"})

        return render(request,'enroll/userregistration.html',{'form':fm})
```

### Ordering form fields in django

By default order_fields=None but we can change it according to our need

```python
    from .forms import StudentRegistration

    def showformdata(request):
        fm=StudentRegistration()

        # It will display first email then name
        fm.order_fields(field_order=['email','name'])

        return render(request,'enroll/userregistration.html',{'form':fm})
```

## Loop form

## Form Field Arguments

1. required --> takes True/False
2. label --> you can set (label="Enter Name")
3. label_suffix --> override's the form default suffix
4. initial --> let's set the initial value
5. disabled --> If it's true then user can't edit the value
6. help_text --> It let you set the text which will helpful for field
7. error_messages --> pass in a dictionary with keys matching the error messagee you want ot override

    ```python
        name=forms.CharField(error_messages={'required':"Enter your name"})
    ```

8. validators --> Provides list of validation function for the field
9. localize --> it enables the localization of form input as well as the rendered output.
10. widget --> It specify the widget class to use when rendering the field, It defines the type of input element

* attrs:
  
  * It let's you set the attribute of input field

    ```python
        feedback=forms.CharField(widget=forms.TextInput(attrs={"class":"class1 class2",'id':'unique'}))
    ```

  * TextINput

    ```python
            name=forms.CharField(widget=forms.TextInput)
    ```

  * NumberInput
  * EmailInput
  * URLInput
  * PasswordInput

## What is Cross Site Request Forgery (CSRF/XSRF)

Cross-Site Request Forgery (CSRF) is an attack that forces authenticated users to submit a request to a Web application against which they are currently authenticated.

## GET Form Data and Validate Data in Django

### is_valid()

It is used to run validation whether data is valid or not depending upon Boolean Value

```python
        # syntax:
        Form.is_valid()
```

### cleaned_data

This attribute is used to access clean data, The validated data is called clean data.

### Get Django form data in terminal

In views.py define view which will get the form data and show the form in template

```python
    from .forms import StudentRegistration

    def showformdata(request):
        if request.method=='POST':
            fm=StudentRegistration(request.POST)
            if fm.is_valid():
                name=fm.cleaned_data['name']
                email=fm.cleaned_data['email']
            else:
                fm=StudentRegistration()
        
        return render(request,"page.html",{'form':fm})
```

## HttpResponseRedirect

## Form Field

## CharField

* CharField(**kwargs)  
* Default widget: TextInput  
* Empty value: Whatever you've given as empty_value.  
* Normalize to: string  
* Uses MaxLengthValidator and MinLengthValidator if max_length and min_length are provided. Otherwise all inputs are valid.
* Error message keys: required, max_length,min_length
* strip - If True(default), the value will be stripped
* empty_value: The value to use to represent "emtpy".Degaults to an emtpy string

    ```python
        name=forms.CharField(min_length=5,max_length=50,error_message={"required":"Enter your name"})
    ```

## BooleanField

* BooleanField(**kwargs)
* Default widget: CheckboxInput
* Empty value: False
* Noramlizes to: A python Ture or False
* Validates the value is True
* Error message keys: required

    ```python
        agree = forms.BooleanField(label="I agree")
    ```

## Integer field

## Decimal field

## Flaot field

## Cleaning and validating specific form field in django

It is for customize data properties and input

```python
    from django import forms

    class StudentRegistration(forms.Form):
        name=forms.CharField()
        email=forms.EmailField()
        password=forms.CharField(widget=forms.PasswordInput)

        # To validate name length manually 

        def clean_name(self):
            valname=self.cleaned_data['name'] | valname=self.cleaned_data.get('name')

            if len(valname)<4:
                raise forms.ValidationError("Enter more than or equal to 4")
            
            return valname 
```

## Validation of Complete Django form at once

60th video

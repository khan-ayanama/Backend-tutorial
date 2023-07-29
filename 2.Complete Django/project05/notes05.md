# Notes - 05

In form API we face repetition of code in model and form in order to optimze it we use Model form in which case we need to define all the form field in model and inherit it in form.

```python
    class Registration(forms.ModelForm):
        class Meta:
            model=User
            fields=['name','password','email']
```

If the model field has blank=True, then required is set False in the form field

## labels in model form

```python
    class Registration(forms.ModelForm):
        class Meta:
            model=User
            fields=['name','password','email']

            labels={'name':'Enter Name','password':"Enter password",'email':"Enter Email"}
            
            help_text={'name':"Enter your full name"}

            error_messages={'name':{'required':"Naam likhna jaruri hai"}}

            widgets={'password':forms.PasswordInput,
                'name':forms.TextInput(attrs={'class':'myclass','placeholder':'yaha naam likhe'})
            }
```

## Extra Validator to Model form Field

```python
    class Registration(forms.ModelForm):

        # Add extra validator here
        name=forms.CharField(max_length=50,required=False)

        class Meta:
            model=User
            fields=['name','password','email']

            labels={'name':'Enter Name'}
            
            widgets={'password':forms.PasswordInput}
```

## save() Method

save(commit=False/True) Method --> This method creates and save a database object from the data bound to the form

## Dynamic URL

Refer to wscube tutorial

### Custom path convertor

video 67

### Selecting form field in model form

* We can write __all__ instead of fields in form

    ```python
        class Registration(forms.ModelForm):
            class Meta:
                model=User
                # fields=['name','password','email']

                fields='__all__'
    ```

* We can exclude cetain field

```python
    class Registration(forms.ModelForm):
        class Meta:
            model=User
            # fields=['name','password','email']

            exclude=['name']
```

## Model form inheritance

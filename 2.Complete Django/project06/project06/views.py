from django.shortcuts import  render
from django.contrib.auth.forms import UserCreationForm

def sign_up(request):
    if request.method == 'POST':
        fm = UserCreationForm()
        if fm.is_valid():
            fm.save()
    else:
        fm=UserCreationForm()
    return render(request,'index.html',{'form':fm})

def data_set(request):
    ConnectionResetError(request,'Index.html')
    return render(request,'index.html')

def full_name(request):
    if request.method=='POST':
        first_name=request.get.POST('fname')
        last_name=request.get.POST('lname')
        full_name=first_name+last_name
    
    return render(request,'index.html',{'full_name':full_name})
from django.shortcuts import render, redirect
from django.contrib.auth.models import User # this is a build in model 
from django.contrib.auth import login as authlogin ,logout as authlogout 
from django.contrib.auth import authenticate



# Create your views here.
def signup(request):
    user=None
    error_msg=None
    if request.POST:
        username=request.POST['username']
        password=request.POST['password']
        print(f'username:{username} and password: {password}')
    try:
        user=User.objects.create_user(username=username, password=password)# USer is  a buildin model
    except Exception as e:
        error_msg=str(e)
    
    return render(request, 'users/create.html', {'user':user, 'error': error_msg} )


def login (request):
    err_msg=None
    if request.POST: 
        username=request.POST['username'] #: Using square brackets (e.g., request.POST['username']) directly retrieves the value associated with the 'username' key from the POST data.
        password=request.POST['password']
        user=authenticate(username=username, password=password)#If a match is found, it returns a User object representing the user.
        if user:#if user checks if authenticate() returned a valid user.
            print(user)
            authlogin(request, user)# If the user is valid, this function from django.contrib.auth logs the user in and starts a session.
            #It links the user to the current session and stores the session data server-side.
            return redirect('list')
        else:
            err_msg='invalid name or password'


    return render(request, 'users/login.html', {'error':err_msg})

def logout(request):
    authlogout(request) #his function from django.contrib.auth logs the user out by clearing any user-related session data.
    return redirect('login')#No user argument required: The logout function only needs the request object because Django knows who the current user is based on the session data associated with the request

    


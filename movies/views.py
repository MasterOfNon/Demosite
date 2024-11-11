from django.shortcuts import render
from .models import Movieinfo
from .form import Movieform
from django.contrib.auth.decorators import login_required
# Create your views here.
def create(request):
    if request.POST:
        frm= Movieform(request.POST, request.FILES) # #This line creates an instance of the Movieform using the data that the user submitted (request.POST). This form instance now holds the data the user has entered and allows us to validate it.
        if frm.is_valid():
            frm.save()# this line saves the data to the database. Django's save() method on the form will create a new record in the database using the information provided in the form.
            
    else:
            frm=Movieform() # jsut shows a form.
    

    #if request.POST: 
        #print(request.POST)# this gives whole data
       # title=request.POST.get('title') # must match the name in template's form's label 
       # year= request.POST.get('year')
       #summary=request.POST.get('summary')
       #obj=Movieinfo(title=title, year=year, summary=summary) # for storing in db
       #obj.save()
    
    return render(request,'create.html', {'frm':frm})

@login_required(login_url='login/')
def list(request):
    recent_visits=request.session.get('recent_visits', [])#This allows the app to remember the movies a user has recently viewed or interacted with across different page visits. If a new user or a user without a recent_visits session visits, the list will simply be empty.

   
    count=int(request.session.get('count',0))#This line tries to retrieve a session variable called "count" (stored on the server side for this specific user).
    count=count+1
    request.session['count']=count #. This step stores the new count in the user's session data, which Django manages on the server side.
    #print(request.COOKIES) # request.COOKIES is a dictionary that contains all the cookies sent by the user's browser.
    #visits= int (request.COOKIES.get('visits', 0))# request.COOKIES.get('visits', 0) tries to get the value of the "visits" cookie.
                                                    #If "visits" doesn't exist, it defaults to 0.
                                                    # int(...) converts the cookie value from a string to an integer, so we can work with it as a number.
    #visits=visits+1
    recent_m=Movieinfo.objects.filter(pk__in=recent_visits)#Retrieves movie records where their primary keys (pk) are present in the recent_visits list
    movie_set= Movieinfo.objects.all().order_by('year')# shows to user
    print(movie_set)
    response=render(request,'list.html', {'recent_m_set':recent_m,'movies':movie_set,'visits':count})
    #response.set_cookie('visits', visits)# The server may set a cookie in the user's browser using Set-Cookie in the HTTP headers.
    return response

@login_required(login_url='login/')
def edit(request, pk):

    instance_edit= Movieinfo.objects.get(pk=pk) # gets the data from the db
    if request.POST:
         frm=Movieform(request.POST, instance=instance_edit) #Movieform is the form class linked to the Movieinfo model, which holds the structure for editing a movie.
        #purpose: This line is used when the user submits the form with new data, and you want to both keep the original object (instance_edit) and update it with the new data provided by the user.                                                     #request.POST: This contains the data that the user submitted in the form (like the new movie title, year, and summary).
                                                             #instance=instance_edit: This tells Django that we are editing an existing movie (not creating a new one). It pre-fills the form with the current data of the movie.
                                                             #This line combines the updated form data (request.POST) with the existing movie data (instance_edit).
         if frm.is_valid():
              frm.save()
    # alternative code_____
         #title= request.POST.get('title')# gets the title form the user http 
         #year= request.POST.get('year')
         #summary= request.POST.get('summary')
         #instance_edit.title=title # makes changes in the object
         #instance_edit.year=year
         #instance_edit.summary=summary
         #instance_edit.save()
    else:
        recent_visits=request.session.get('recent_visits',[])
        recent_visits.insert(0,pk) #Adds the primary key (pk) of the movie being edited to the start of the recent_visits list. This keeps the most recently edited movie at the front of the list.
        request.session['recent_visits']=recent_visits#save to server
        frm= Movieform(instance=instance_edit) #this line is used to pre-fill the form with existing data from the database.
        #t is typically used when the user first opens the form to edit an existing object (in this case, a movie), but no changes have been submitted yet.

    return render(request,'create.html', {'frm':frm})# here edit.html fiel is not given as it doesnot contain form

@login_required(login_url='login/')
def delete(request, pk):# request: This contains all the information about the HTTP request made by the user (whether it’s a GET or POST request, user data, etc.).
    instance=Movieinfo.objects.get(pk=pk)#objects.get(pk=pk) is a Django method used to retrieve a specific row (or movie) from the database where the primary key (pk) matches the one passed into the function.
    instance.delete()
    movie_set= Movieinfo.objects.all()# shows all data
    print(movie_set)#This line is for debugging purposes. It prints all the remaining movies to the console so the developer can see them.
    return render(request,'list.html', {'movies':movie_set})




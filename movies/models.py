from django.db import models

# Create your models here. data management happens  here that is class will be table.
class Censorinfo(models.Model):# this class must be before the class it is being used for in realtion.
    rating=models.CharField(max_length=200, null=True)
    certified_by=models.CharField(max_length=200, null=True)

    def __str__(self):
        return f" rating:{self.rating} and is certified by {self.certified_by}"

class Director(models.Model):
    name=models.CharField(max_length=100)

    def __str__(self):
        return f" director name:{self.name}"
    
class Actor (models.Model):
    name=models.CharField(max_length=100)

    def __str__(self):
        return f" Main lead:{self.name}"
    
class Movieinfo(models.Model):
    title= models.CharField(max_length=250) 
    year= models.DateField()
    summary= models.TextField(max_length=1000)
    #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@OneToOne@@@@@@@@@@@@@@@@@@@
    poster= models.ImageField(upload_to='image/', null=True, blank=True) #This argument allows the poster field to accept NULL values in the database.
    censordetails= models.OneToOneField(Censorinfo, on_delete=models.SET_NULL, related_name='movie', null=True) #This allows the censordetails field to be empty or NULL in the database.
    #SET_NULL means that if the associated Censorinfo entry is deleted, Django will set censordetails to NULL (no value) instead of deleting the Movieinfo entry as well.
    # related_name is an optional argument that defines the name of the reverse relation from Censorinfo back to Movieinfo.
    #If you have an instance of Censorinfo, you can access the related Movieinfo instance by calling censorinfo_instance.movie (using movie as the reverse lookup).
    #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@One To Many@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
    directedby=models.ForeignKey(Director, on_delete=models.SET_NULL, related_name='director', null=True)
    #@@@@@@@@@@@@@@@@@ManytoMAny@@@@@@@@@@@@@@@@
    acters=models.ManyToManyField(Actor, related_name='acted_movies')

    def __str__(self):# str__ method: The __str__ method tells Django how to display the object when you try to print it or show it in the Django admin, shell, etc. By defining the __str__ method, you control what details are shown.
        return f"{self.title} image= {self.poster} released on {self.year} with summary: {self.summary}"


    

 
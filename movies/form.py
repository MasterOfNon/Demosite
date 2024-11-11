from django.forms import ModelForm
from .models import Movieinfo
from django.forms.widgets import SelectDateWidget

class Movieform(ModelForm):
    class Meta: # describes the properties of the class/table
        model= Movieinfo #  does not include parentheses () because it is simply referring to the model class itself, not creating an instance of that class.
        fields= '__all__'# This line is telling Django which model class (Movieinfo) should be used to create the form. It is a reference to the model class, not an instance of it.
        widgets = {
            'year': SelectDateWidget(years=range(1980, 2025)),  # Customize the range as needed
        }


                               
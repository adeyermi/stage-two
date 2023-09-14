from django import forms  
from crud.models import Crud
from django.forms import fields

class CrudForm(forms.ModelForm):  
    class Meta:  
        model = Crud  
        fields = "__all__"  
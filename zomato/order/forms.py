
from django.forms import ModelForm
from .models import order, userregister

class kim(ModelForm):
    class Meta:
        model=order
        fields=['name','number','food','address']

#new class 
class jim(ModelForm):
    class Meta:
        model=userregister
        fields=['fullname','username','email','password','num']
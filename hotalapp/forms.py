from django import forms 
from .models import cust,data

class AddCust(forms.ModelForm):
    class Meta:
        model=cust
        
        fields=('firstname','lastname','phonenumber','email','state','username','password')


        widgets={
           'firstname':forms.TextInput(attrs={'class':'form-contro'}),
           'lastname':forms.TextInput(attrs={'class':'form-contro'}),
           'phonenumber':forms.TextInput(attrs={'class':'form-contro'}),
           'email':forms.TextInput(attrs={'class':'form-contro'}),
           'state':forms.TextInput(attrs={'class':'form-contro'}),
           'username':forms.TextInput(attrs={'class':'form-contro'}),
           'password':forms.TextInput(attrs={'class':'form-contro'}),

    }

class DataForm(forms.ModelForm):
    class Meta:
        model=data
        
        fields=('room_id','amount','bed_space','details','type','image')


        widgets={
            
           'room_id':forms.TextInput(attrs={'class':'form-contro'}),
           'amount':forms.TextInput(attrs={'class':'form-contro'}),
           'bed_space':forms.TextInput(attrs={'class':'form-contro'}),
           'details':forms.TextInput(attrs={'class':'form-contro'}),
           'type':forms.TextInput(attrs={'class':'form-contro'}),
           'image':forms.FileInput(attrs={'class':'form-contro'}),
          
           

    }          
        

     
    
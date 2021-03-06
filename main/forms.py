from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User
from django import forms

from .models import Comp


class AuthForm (AuthenticationForm):
    username = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={'placeholder': 'Username'}))
    password = forms.CharField(required=True, widget=forms.widgets.PasswordInput(attrs={'placeholder': 'Password'}))

    class Meta:
        fields = ['username', 'password']
        # model = User


class RegistrationForm (UserCreationForm):
    username = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={'placeholder': 'Username'}))
    password1 = forms.CharField(required=True, widget=forms.widgets.PasswordInput(attrs={'placeholder': 'Password'}))
    password2 = forms.CharField(required=True, widget=forms.widgets.PasswordInput(attrs={'placeholder': 'Password Confirmation'}))
     
    class Meta:
        fields = ['username', 'password1', 'password2']
        model = User
        
        
class AddCompForm(forms.Form):
    name = forms.CharField(required=True, 
        widget=forms.widgets.TextInput(
            attrs={'placeholder': 'Name', 'id': 'new_rec_name', 'maxlength': '49'}           
        ),
        error_messages={'required': 'Please enter a comp name'},
        label='Computer name'
    )
      
    cpu = forms.CharField(
        widget=forms.widgets.TextInput(
            attrs={'placeholder': 'CPU', 'id': 'new_rec_country', 'maxlength': '29'}
        ),
        error_messages = {'required': 'Please input cpu'},
        label = 'CPU'
    )
    
    rate = forms.IntegerField(required=True,
        widget=forms.widgets.NumberInput(
            attrs={'placeholder': 'Rate', 'id': 'new_rec_sportType', 'onKeyUp': 'if(this.value>5){this.value="5";}else if(this.value<0){this.value="0";}'}
        ),
        error_messages={'required': 'Please input rate'},
        label='Rate'
    )
    
    price = forms.IntegerField(required=True,
        widget=forms.widgets.NumberInput(
            attrs={
                'placeholder': 'Price',
                'id': 'new_rec_prizeCount', 
                'onKeyUp': 'if(this.value>999999){this.value="999999";}else if(this.value<0){this.value="0";}'
            }
        ),
        error_messages={'required': 'Please input price'},
        label='Price'
    )    

    desc = forms.CharField(required=True,
        widget=forms.widgets.Textarea(
            attrs={'placeholder': 'Description', 'id': 'new_rec_desc', 'maxlength': '1999'}
        ),
        error_messages={'required': 'Please input short description'},
        label='Description'
    )

    image = forms.FileField(required=False,
        widget=forms.widgets.ClearableFileInput(
            attrs={'accept':'image/jpeg, image/png, image/gif', 'id':'new_rec_img'}
        )
    )

    def fill_object(self):
        return Comp.objects.create(
            name = self.cleaned_data['name'],
            cpu = self.cleaned_data['cpu'],
            rate = int(self.cleaned_data['rate']),
            price = int(self.cleaned_data['price']),
            desc = self.cleaned_data['desc']
        )
    
    
    
from django import forms
from django.contrib.auth.models import User
from . import models


class CustomerUserForm(forms.ModelForm):
    class Meta:
        model=User
        fields=['first_name','last_name','username','password']
        widgets = {
        'password': forms.PasswordInput()
        }
        
class CustomerForm(forms.ModelForm):
    class Meta:
        model=models.Customer
        fields=['address','mobile','profile_pic']

class ProductForm(forms.ModelForm):
    class Meta:
        model=models.Product
        fields=['brand','model','network_technology','t2G_bands','t3G_bands',
        't4G_bands','network_speed','GPRS','EDGE','announced','status','dimentions','weight_g',
        'weight_oz','SIM','display_type','display_resolution','display_size','OS','CPU','Chipset',
        'GPU','memory_card','internal_memory','RAM','primary_camera','secondary_camera','loud_speaker','audio_jack',
        'WLAN','bluetooth','GPS','NFC','radio','USB','sensors','battery',
        'colors','approx_price','img_url']

#address of shipment
class AddressForm(forms.Form):
    Email = forms.EmailField()
    Mobile= forms.IntegerField()
    Address = forms.CharField(max_length=500)

class FeedbackForm(forms.ModelForm):
    class Meta:
        model=models.Feedback
        fields=['name','feedback']

#for updating status of order
class OrderForm(forms.ModelForm):
    class Meta:
        model=models.Orders
        fields=['status']

#for contact us page
class ContactusForm(forms.Form):
    Name = forms.CharField(max_length=30)
    Email = forms.EmailField()
    Message = forms.CharField(max_length=500,widget=forms.Textarea(attrs={'rows': 3, 'cols': 30}))

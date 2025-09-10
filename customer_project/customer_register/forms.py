from django import forms
from .models import Customer

class CustomerForm(forms.ModelForm):

    upload_photo = forms.ImageField()

    class Meta:
        model = Customer
        fields = ('name', 'phone_number')  
        labels = {
            'name': 'Full Name',
            'phone_number': 'Phone Number',
            'upload_photo': 'Booklist'
        }
    
    def __init__(self, *args, **kwargs):
        super(CustomerForm, self).__init__(*args, **kwargs)
        

from django import forms
from .models import Account

class RegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Create password', "class": "form-control"}))
    confirm_password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Confirm password',"class": "form-control"}))

    class Meta:
        model = Account
        fields = ( 'first_name', 'last_name', 'phone_number','email', 'password', 'confirm_password')

    def __init__(self, *args, **kwargs):
        super(RegistrationForm, self).__init__(*args, **kwargs)
        self.fields['first_name'].widget.attrs['placeholder']='Enter First Name'
        self.fields['last_name'].widget.attrs['placeholder']='Enter Last Name'
        self.fields['email'].widget.attrs['placeholder']='Enter Email'
        self.fields['phone_number'].widget.attrs['placeholder']='Enter Phone Number'
        for field in self.fields:
            self.fields[field].widget.attrs['class']='form-control'
            
            
        # self.fields['first_name'].widget.attrs.update({'placeholder': 'First Name', "class": "form-control"})
        # self.fields['last_name'].widget.attrs.update({'placeholder': 'Last Name', "class": "form-control"})
        # self.fields['username'].widget.attrs.update({'placeholder': 'Username', "class": "form-control"})
        # self.fields['email'].widget.attrs.update({'placeholder': 'Email', "class": "form-control"})
        # self.fields['phone_number'].widget.attrs.update({'placeholder': 'Phone Number', "class": "form-control"})


    def clean(self):
        cleaned_data = super(RegistrationForm,self).clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        if password != confirm_password:
            raise forms.ValidationError("Passwords do not match.")
        
        return cleaned_data
    
    def clean_email(self):
        email = self.cleaned_data.get('email')
        if Account.objects.filter(email=email).exists():
            raise forms.ValidationError("Email already exists.")
        return email  
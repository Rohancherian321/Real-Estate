from django import forms
from proapp.models import Ownerreg,Buyerreg,Property, Brqst,Purchase
from django.forms import PasswordInput

class Ownerform(forms.ModelForm):
    class Meta:
        model = Ownerreg
        exclude = ['oid','is_verified']
        widgets = {
            'password': PasswordInput(),
        }

class BuyerregForm(forms.ModelForm):
    class Meta:
        model = Buyerreg
        fields = '__all__'
        exclude = ['bid']
        widgets = {
            'password': PasswordInput(),
        }
    def clean_phoneno(self):
        phoneno = self.cleaned_data.get('phoneno')
        if phoneno and len(str(phoneno)) < 9:
            raise forms.ValidationError("Phone number must have at least 9 digits.")
        return phoneno

    def clean_username(self):
        username = self.cleaned_data.get('username')
        if username and len(username) < 5:
            raise forms.ValidationError("Username must have at least 5 characters.")
        return username

    def clean_password(self):
        password = self.cleaned_data.get('password')
        if password and len(password) < 8:
            raise forms.ValidationError("Password must have at least 8 characters.")
        return password

class Brequestform(forms.ModelForm):
    class Meta:
        model = Brqst
        fields = ['rqno','rqdate','bid','bname','pid','price','qprice']
class Purchaseform(forms.ModelForm):
    class Meta:
        model = Purchase
        fields= ['pno','pdate','pid','bid','bname','cardno','amtpaid']

class PropertyForm(forms.ModelForm):
    class Meta:
        model = Property
        fields= fields = ['oname','ptype','ttype','price','state','district','town','pincode','email','phoneno','builtarea','p1','p2','p3','des']
        def clean_price(self):
            price = self.cleaned_data.get('price')
            if price is not None and price <= 0:
                raise forms.ValidationError("Price must be a positive value.")
            return price

        def clean_pincode(self):
            pincode = self.cleaned_data.get('pincode')
            if pincode is not None and len(str(pincode)) != 6:
                raise forms.ValidationError("Pin code must be a 6-digit value.")
            return pincode

        def clean_phoneno(self):
            phoneno = self.cleaned_data.get('phoneno')
            if phoneno is not None and len(str(phoneno)) < 9:
                raise forms.ValidationError("Phone number must have at least 9 digits.")
            return phoneno

        def clean_builtarea(self):
            builtarea = self.cleaned_data.get('builtarea')
            if builtarea is not None and builtarea <= 0:
                raise forms.ValidationError("Built area must be a positive value.")
            return builtarea

        def clean(self):
            cleaned_data = super().clean()
            ttype = cleaned_data.get('ttype')
            otype = cleaned_data.get('otype')

            if ttype == 'BUY' and otype == 'FIRST OWNER':
                raise forms.ValidationError("Invalid combination of transaction type and ownership type.")

            return cleaned_data

     
       
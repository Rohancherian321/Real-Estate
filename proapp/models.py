from django.db import models
from django.core.validators import RegexValidator
from datetime import date
from django import forms


class Ownerreg(models.Model):
    oid=models.IntegerField("Owner ID",primary_key=True)
    oname=models.CharField("Owner Name",max_length=25)
    phoneno_regex = RegexValidator(
        regex=r'^\+?1?\d{9,15}$',
        message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed."
    )
    phoneno=models.IntegerField("Phone No",validators=[phoneno_regex])
    email=models.EmailField("Email")
    address=models.CharField("Address",max_length=250)
    photo=models.ImageField("ID Proof",upload_to='images/')
    username=models.CharField("User Name",max_length=25,unique='true')
    password=models.CharField("Password",max_length=25)
    is_verified=models.BooleanField(default=False)



class Buyerreg(models.Model):
    bid=models.IntegerField("Buyer ID",primary_key=True)
    bname=models.CharField("Buyer Name",max_length=25)
    phoneno_regex = RegexValidator(
        regex=r'^\+?1?\d{9,15}$',
        message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed."
    )
    phoneno=models.IntegerField("Phone No",validators=[phoneno_regex])
    email=models.EmailField("Email")
    address=models.CharField("Address",max_length=250)
    username=models.CharField("User Name",max_length=25,unique='true')
    password=models.CharField("Password",max_length=25)
    

class Property(models.Model):
    user=models.ForeignKey(Ownerreg,on_delete=models.CASCADE,null=True)
    pid=models.IntegerField("Property ID",primary_key=True)
    
    oname=models.CharField("Owner Name",max_length=30)
    PROPRTYPE_CHOICES = (
        ('Residential Apartment','Residential Apartment'),
        ('Residential Land','Residential Land'),
        ('Residential House/Villa','Residential House/Villa'),
        ('Residential Other','Residential Other'),
        ('Commercial Shop','Commercial Shop'),
        ('Comercial Office','Comercial Office'),
        ('Commercial Land','Commercial Land'),
        ('Commercial Building','Commercial Building'),
        ('Commercial Other','Commercial Other'),
        ('Industrial Building','Industrial Building'),
        ('Industrial Land','Industrial Land'),
        ('Agricultural Land','Agricultural Land')
    )
    ptype=models.CharField("Property Type",max_length=50,choices=PROPRTYPE_CHOICES)
    TRANSACTION_CHOICES = (
        ('BUY','BUY'),
        ('RENT','RENT')
    )
    ttype=models.CharField("Transacaction Type",max_length=10,choices=TRANSACTION_CHOICES)
    
    price=models.IntegerField("Price")
    des=models.CharField("Description",max_length=500)
    state=models.CharField("State",max_length=6,default='Kerala')
    DIST_CHOICES = (
        ('Alappuzha','Alappuzha'),
        ('Eranakulam','Eranakulam'),
        ('Iduki','Iduki'),
        ('Kannur','Kannur'),
        ('Kasaragod','Kasaragod'),
        ('Kollam','Kollam'),
        ('Kottayam','Kottayam'),
        ('Kozhikode','Kozhikode'),
        ('Malappuram','Malappuram'),
        ('Palakkad','Palakkad'),
        ('Pathanamthiita','Pathanamthiita'),
        ('Thiruvananthapuram','Thiruvananthapuram'),
        ('Thrissur','Thrissur'),
        ('Wayanad','Wayanad')
    )
    
    district =models.CharField("District",max_length=20,choices=DIST_CHOICES)
    town=models.CharField("Town",max_length=20)
    pincode=models.IntegerField("Pin Code")
    email=models.EmailField("Email")
    phoneno_regex = RegexValidator(
        regex=r'^\+?1?\d{9,15}$',
        message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed."
    )
    phoneno=models.IntegerField("Phone NO",validators=[phoneno_regex])
    builtarea=models.IntegerField("Built Area")
    p1=models.ImageField("Photo1",upload_to='property/')
    p2= models.ImageField("Photo2", upload_to='property/')
    p3= models.ImageField("Photo5", upload_to='property/')
   
    rights=models.CharField("State Of Property",max_length=2,default='NS')
class Brqst(models.Model):
    rqno=models.IntegerField("Request No",primary_key=True)
    rqdate=models.DateField("Request Date", default=date.today)
    bid=models.IntegerField("Buyer ID")
    oid=models.IntegerField("Owner ID",default=0)
    bname=models.CharField("Buyer Name",max_length=20)
    pid=models.IntegerField("Propertyid")
    price=models.IntegerField("price",default=0)
    qprice=models.IntegerField("Requested Price")
    rights=models.CharField("Rights",default='NS',max_length=3)

class Purchase(models.Model):
    pno=models.IntegerField("Purchase NO")
    rqno=models.IntegerField("Request No",default=0)
    pdate=models.DateField("Purchase Date",default=date.today)
    pid=models.IntegerField("Property ID")
    oid=models.IntegerField("Owner ID",default=0)
    bid=models.IntegerField("Buyer ID")
    bname=models.CharField("Buyer Name",max_length=30)
    price = models.IntegerField("Actual Price",default=0)
    amtpaid=models.IntegerField("Amount Paid")
    cardno=models.CharField("Card NO",max_length=30)

class Trend(models.Model):
    pid=models.IntegerField("Property ID")
    oname=models.CharField("Owner Name",max_length=20,default='x')
    tcount=models.IntegerField("No Of Counts",default=0)

class Book(models.Model):
    user=models.ForeignKey(Buyerreg,on_delete=models.CASCADE)
    owner=models.ForeignKey(Ownerreg,on_delete=models.CASCADE)
    prop=models.ForeignKey(Property,on_delete=models.CASCADE)
    status=models.CharField(max_length=100)
    time=models.DateTimeField(auto_now=True)
    app_date=models.DateField(null=True)


class PropertySearchForm(forms.Form):
    district = forms.CharField(required=False)
    pttype = forms.CharField(required=False)
  
   

    # Add more fields as needed for other search criteria


# Create your models here.

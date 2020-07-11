from django.db import models
from django.utils import timezone
from phonenumber_field.modelfields import PhoneNumberField
from django.contrib.auth.models import User
#from django.db.backends.mysql import hospital_employee


# Create your models here.

class Example(models.Model):
    class Meta:
    #managed = False # remove this line
        db_table = 'hospital_employee'
        
    he_id = models.AutoField(primary_key = True,)       
    he_hospital_id=models.CharField(max_length=100,null=True)
    he_name=models.CharField(max_length=100)
    he_type=models.CharField(max_length=20)
    he_mobile=models.IntegerField(null=True)
    enable_otp=models.CharField(max_length=20,null=True)
    he_otp=models.IntegerField(null=True)
    he_is_otp_verify=models.IntegerField(null=True)
    status=models.TextField()
    formstatus=models.CharField(max_length=100,null=True)
    he_date=models.DateField(auto_now_add=True, null = True, blank = True)

    
    
    def __str__(self):
            return self.he_name
        

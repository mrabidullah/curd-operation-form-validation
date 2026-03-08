from django.db import models

# Create your models here.

class student(models.Model):
    name=models.CharField(max_length=100,null=True)
    F_name=models.CharField(max_length=100,null=True)
    dep_name=models.CharField(max_length=100,null=True)
    Roll_number=models.IntegerField(unique=True)
    address=models.CharField(max_length=1000,null=True)
    email=models.EmailField(unique=True)
    marks=models.FloatField(null=True)
    # sent_at=models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>principal model>>>>>>>>>>>>>>>>>>>>>>>>>>>>
class principle(models.Model):
    first_name=models.CharField(max_length=50,null=True)
    last_name=models.CharField(max_length=50,null=True)
    age=models.IntegerField(null=True)
    email=models.EmailField(unique=True)
  
    def __str__(self):
         return self.first_name
     
     
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>for user message>>>>>>>>>>>>>>>>>>>>>>>>>>>



class PrincipalMessage(models.Model):
    name = models.CharField(max_length=150)
    email = models.EmailField()
    subject = models.CharField(max_length=200, blank=True)
    message = models.TextField()
    sent_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
         return self.name
     
     
# >>>>>>>>>>>>>>>>>>>>>>>>>>  Teachers cantact >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
class Teachers(models.Model):
    name=models.CharField(max_length=30,null=True)
    f_name=models.CharField(max_length=30,null=True)
    P_number=models.IntegerField(max_length=17,null=True)
    email=models.CharField()
    address=models.CharField()
    message=models.TextField()
    sent_at=models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.name
    
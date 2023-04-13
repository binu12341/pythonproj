from django.db import models


# Create your models here.
class Studreg(models.Model):
    susername=models.CharField(max_length=100)
    spassword=models.CharField(max_length=100)
    sadds = models.CharField(max_length=100)
    scity = models.CharField(max_length=100)
    semail = models.CharField(max_length=100)
    sphon = models.IntegerField(null=True,blank=True)
    sgender=models.CharField(max_length=100)
    sgurdianname = models.CharField(max_length=100)
    sgurdianphon = models.IntegerField(null=True,blank=True)
    saadharno=models.IntegerField(null=True,blank=True)
    
class roomselection(models.Model):
    sroomno=models.IntegerField(null=True,blank=True)
    no_of_members=models.IntegerField(null=True,blank=True)
    food_status=models.CharField(max_length=100)
    stayfrom=models.CharField(max_length=100)
    sduration=models.CharField(max_length=100)
    shostel_fee=models.IntegerField(null=True,blank=True)
    
class foodtable(models.Model):
    id = models.CharField(max_length=100,primary_key=True)
    breakfast=models.CharField(max_length=100)
    Lunch=models.CharField(max_length=100)
    Evening=models.CharField(max_length=100)
    Dinner=models.CharField(max_length=100)

class feedback(models.Model):
    feedback_room=models.CharField(max_length=100)
    feedback_mess=models.CharField(max_length=100)

class Securityreg(models.Model):
    security_id = models.IntegerField(primary_key=True)
    security_name=models.CharField(max_length=100)
    security_password=models.CharField(max_length=10)
    security_adds = models.CharField(max_length=100)
    experience = models.IntegerField()
    email = models.CharField(max_length=100)
    phone = models.IntegerField()
    security_gender=models.CharField(max_length=100)
    salary_except=models.IntegerField()





        
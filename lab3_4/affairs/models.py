from django.db import models

# Create your models here.
class user (models.Model):
    id=models.AutoField(primary_key=True)
    first_name=models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    email=models.EmailField(max_length=50)
    password=models.CharField(max_length=20)
    cpassword = models.CharField(max_length=20,null=True)

class Intake(models.Model):
    id=models.AutoField(primary_key=True)
    name = models.CharField(max_length=30)

class Track(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)


class Trainee(models.Model):
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=20)
    bdate=models.DateField()
    promotion=models.DecimalField(max_digits=5,decimal_places=1)
    intake=models.CharField(max_length=20)
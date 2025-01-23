from django.db import models
class Marksheet(models.Model):
    name=models.CharField(max_length=50)
    subject1=models.DecimalField(max_digits=5,decimal_places=2)
    subject2=models.DecimalField(max_digits=5,decimal_places=2)
    subject3=models.DecimalField(max_digits=5,decimal_places=2)
    subject4=models.DecimalField(max_digits=5,decimal_places=2)
    subject5=models.DecimalField(max_digits=5,decimal_places=2)
    subject6=models.DecimalField(max_digits=5,decimal_places=2)
# Create your models here.

from django.db import models

# Create your models here.
class Datas(models.Model):
    Name=models.CharField(max_length=20)
    Age=models.IntegerField()
    Address=models.CharField(max_length=50)
    Contact=models.IntegerField()
    Salary=models.IntegerField()
    Mail=models.CharField(max_length=20)

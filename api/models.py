from django.db import models

# Create your models here.

class Dept(models.Model):
    name=models.CharField(max_length=100,primary_key=True)

    def __str__(self):
        return self.name
    
class Emp(models.Model):
    name=models.CharField(max_length=100)
    age=models.IntegerField()
    email=models.EmailField()
    join_date=models.DateField()
    sal=models.DecimalField(max_digits=7,decimal_places=2)
    dept=models.ForeignKey(Dept,on_delete=models.CASCADE)

    def __str__(self):
        return self.name
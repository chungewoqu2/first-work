from django.db import models

# Create your models here.
class New_table(models.Model):
    id = models.AutoField(primary_key=True)
    name=models.CharField(max_length=20)
    grade=models.CharField(max_length=20)
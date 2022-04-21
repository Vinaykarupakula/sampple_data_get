from django.db import models

# Create your models here.

class employee(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length= 45)
    des = models.CharField(max_length=45)
    dept = models.CharField(max_length=45)

    def __str__(self):
        return self.name

        
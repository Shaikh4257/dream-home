from django.db import models

# Create your models here.


class Contact(models.Model):
    email=models.CharField(max_length=200)
    name=models.CharField(max_length=200)
    contactno=models.CharField(max_length=200)
    description=models.CharField(max_length=200)

    def __str__(self):
        return self.name
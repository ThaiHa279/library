from django.db import models

# Create your models here.

class UserModel(models.Model):
    id = models.IntegerField(primary_key=True, auto_created=True)
    username = models.CharField(max_length=200)
    password = models.TextField()
    name = models.CharField(max_length=200)
    address = models.TextField(blank=True)
    phone = models.CharField(max_length=20, blank=True)
    email = models.CharField(max_length=200)
    class Meta:
        managed = False
        db_table = 'user'
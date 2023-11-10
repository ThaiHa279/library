from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    name = models.CharField(max_length=200)
    address = models.TextField(blank=True)
    phone = models.CharField(max_length=20, blank=True)
    pass

class History(models.Model):
    user_id = models.IntegerField(primary_key=True)  # The composite primary key (user_id, book_id) found, that is not supported. The first column is selected.
    book_id = models.IntegerField()
    borrow_time = models.DateField(blank=True, null=True)
    pay_time = models.DateField(blank=True, null=True)
    status = models.DateField(blank=True, null=True)
    
    class Meta:
        managed = False
        db_table = 'history'
        unique_together = (('user_id', 'book_id', 'status'),)



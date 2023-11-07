from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    name = models.CharField(max_length=200)
    address = models.TextField(blank=True)
    phone = models.CharField(max_length=20, blank=True)
    pass

class Book(models.Model):
    print_isbn = models.TextField(db_column='Print ISBN', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    eisbn = models.TextField(db_column='eISBN', blank=True, null=True)  # Field name made lowercase.
    title = models.TextField(db_column='Title', blank=True, null=True)  # Field name made lowercase.
    subtitle = models.TextField(db_column='Subtitle', blank=True, null=True)  # Field name made lowercase.
    authors = models.TextField(db_column='Authors', blank=True, null=True)  # Field name made lowercase.
    editors = models.TextField(db_column='Editors', blank=True, null=True)  # Field name made lowercase.
    publisher = models.TextField(db_column='Publisher', blank=True, null=True)  # Field name made lowercase.
    disciplines = models.TextField(db_column='Disciplines', blank=True, null=True)  # Field name made lowercase.
    copyright_year = models.IntegerField(db_column='Copyright Year', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    publication_date = models.TextField(db_column='Publication Date', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    frontlist_or_backlist = models.TextField(db_column='Frontlist or Backlist', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    language = models.TextField(db_column='Language', blank=True, null=True)  # Field name made lowercase.
    bisac_codes = models.TextField(db_column='BISAC Codes', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    bisac_literals = models.TextField(db_column='BISAC Literals', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    lc_call_number = models.TextField(db_column='LC Call Number', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    lc_subject_headings = models.TextField(db_column='LC Subject Headings', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    date_available_on_jstor = models.TextField(db_column='Date Available on JSTOR', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    series = models.TextField(db_column='Series', blank=True, null=True)  # Field name made lowercase.
    stable_url = models.TextField(db_column='Stable URL', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    book_id = models.CharField(db_column='Book ID', primary_key=True, max_length=100)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    subject_collections = models.TextField(db_column='Subject Collections', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    cats_id = models.TextField(db_column='CATS ID', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = 'book'


class BookGenres(models.Model):
    book_id = models.CharField(primary_key=True, max_length=255)  # The composite primary key (book_id, genre_id) found, that is not supported. The first column is selected.
    genre_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'book_genres'
        unique_together = (('book_id', 'genre_id'),)




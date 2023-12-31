# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthtokenToken(models.Model):
    key = models.CharField(primary_key=True, max_length=40)
    created = models.DateTimeField()
    user = models.OneToOneField('UserUser', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'authtoken_token'


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


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey('UserUser', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Genres(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'genres'


class UserUser(models.Model):
    id = models.BigAutoField(primary_key=True)
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()
    name = models.CharField(max_length=200)
    address = models.TextField()
    phone = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'user_user'


class UserUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(UserUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'user_user_groups'
        unique_together = (('user', 'group'),)


class UserUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(UserUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'user_user_user_permissions'
        unique_together = (('user', 'permission'),)

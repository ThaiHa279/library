# Generated by Django 4.2.7 on 2023-11-02 03:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserModel',
            fields=[
                ('id', models.IntegerField(auto_created=True, primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=200)),
                ('password', models.TextField()),
                ('name', models.CharField(max_length=200)),
                ('address', models.TextField(blank=True)),
                ('phone', models.CharField(blank=True, max_length=20)),
                ('email', models.CharField(max_length=200)),
            ],
            options={
                'db_table': 'user',
                'managed': False,
            },
        ),
    ]
# Generated by Django 3.2.8 on 2022-02-12 17:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_rename_user_registeruser'),
    ]

    operations = [
        migrations.AddField(
            model_name='registeruser',
            name='cpassword',
            field=models.CharField(default='', max_length=50),
        ),
    ]
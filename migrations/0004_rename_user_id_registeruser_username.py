# Generated by Django 3.2.8 on 2022-02-13 03:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_registeruser_cpassword'),
    ]

    operations = [
        migrations.RenameField(
            model_name='registeruser',
            old_name='user_id',
            new_name='username',
        ),
    ]
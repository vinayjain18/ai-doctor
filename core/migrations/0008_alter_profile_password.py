# Generated by Django 4.0.2 on 2022-02-10 14:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_remove_profile_user_profile_password'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='password',
            field=models.CharField(default='12345', max_length=200),
        ),
    ]

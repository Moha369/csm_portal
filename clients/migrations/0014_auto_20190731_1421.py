# Generated by Django 2.2.3 on 2019-07-31 14:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0013_auto_20190731_1414'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='client_API_login',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='post',
            name='client_API_password',
            field=models.CharField(default='', max_length=100),
        ),
    ]

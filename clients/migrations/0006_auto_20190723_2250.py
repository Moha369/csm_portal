# Generated by Django 2.2.3 on 2019-07-23 22:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0005_auto_20190723_2132'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='client_FTP',
            field=models.CharField(default='ftp://', max_length=100),
        ),
        migrations.AlterField(
            model_name='post',
            name='client_password',
            field=models.CharField(default='***', max_length=100),
        ),
    ]
# Generated by Django 2.2.3 on 2019-07-23 21:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0003_auto_20190718_1933'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='client_linkedinurl',
            field=models.CharField(default='wwww.', max_length=150),
        ),
    ]
# Generated by Django 2.2.3 on 2019-07-31 12:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0007_auto_20190730_1750'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='client_salesforceurl',
            field=models.CharField(default='Salesforce Profile...', max_length=150),
        ),
    ]

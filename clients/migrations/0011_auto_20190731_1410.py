# Generated by Django 2.2.3 on 2019-07-31 14:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0010_auto_20190731_1408'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='client_products',
            field=models.CharField(choices=[('analytics', 'Analytics Only'), ('datasets', 'Datasets Only'), ('analytics_datasets', 'Analytics & Datasets'), ('mrt', 'Media Ratings Tool')], max_length=100),
        ),
    ]

# Generated by Django 3.1.3 on 2020-12-22 01:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('create', '0002_auto_20201221_2053'),
    ]

    operations = [
        migrations.AddField(
            model_name='bill_of_sale',
            name='document_name',
            field=models.CharField(default='Document name', max_length=20),
        ),
    ]
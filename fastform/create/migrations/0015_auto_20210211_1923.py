# Generated by Django 3.1.3 on 2021-02-12 00:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('create', '0014_auto_20210209_2114'),
    ]

    operations = [
        migrations.AlterField(
            model_name='billofsale',
            name='document_name',
            field=models.CharField(default='Bill of Sale', max_length=20),
        ),
    ]
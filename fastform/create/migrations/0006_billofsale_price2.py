# Generated by Django 3.1.3 on 2020-12-30 01:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('create', '0005_auto_20201228_1256'),
    ]

    operations = [
        migrations.AddField(
            model_name='billofsale',
            name='price2',
            field=models.CharField(blank=True, max_length=20),
        ),
    ]

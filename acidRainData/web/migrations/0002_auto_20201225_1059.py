# Generated by Django 3.1.4 on 2020-12-25 02:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='county',
            name='name',
            field=models.CharField(max_length=10),
        ),
    ]

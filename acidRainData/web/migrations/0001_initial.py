# Generated by Django 3.1.4 on 2020-12-24 19:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='County',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10, verbose_name='縣市')),
            ],
        ),
        migrations.CreateModel(
            name='RainData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('siteId', models.CharField(max_length=5, verbose_name='測站代碼')),
                ('siteName', models.CharField(max_length=5, verbose_name='測站名稱')),
                ('itemId', models.CharField(max_length=5, verbose_name='測項代碼')),
                ('itemName', models.CharField(max_length=10, verbose_name='測項名稱')),
                ('itemEngName', models.CharField(max_length=20, verbose_name='測項英文名稱')),
                ('itemUnit', models.CharField(max_length=10, verbose_name='測項單位')),
                ('monitorDate', models.CharField(max_length=20, verbose_name='監測日期')),
                ('time', models.DateTimeField(auto_now=True)),
                ('concentration', models.FloatField(verbose_name='數值')),
                ('county', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='web.county')),
            ],
        ),
    ]
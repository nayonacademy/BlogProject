# Generated by Django 2.1.7 on 2019-04-11 04:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0004_blogpost_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='category_status',
            field=models.CharField(choices=[('ACTIVATE', '1'), ('INACTIVATE', '0')], max_length=3),
        ),
    ]

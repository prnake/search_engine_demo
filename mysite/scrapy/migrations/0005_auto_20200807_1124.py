# Generated by Django 3.0.3 on 2020-08-07 11:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('scrapy', '0004_auto_20200807_1123'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='name',
            new_name='title',
        ),
    ]

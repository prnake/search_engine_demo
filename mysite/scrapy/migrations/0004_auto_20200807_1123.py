# Generated by Django 3.0.3 on 2020-08-07 11:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scrapy', '0003_auto_20200807_1039'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='title',
            new_name='name',
        ),
        migrations.AlterField(
            model_name='post',
            name='class_id',
            field=models.CharField(blank=True, max_length=20, verbose_name='课程编号'),
        ),
    ]
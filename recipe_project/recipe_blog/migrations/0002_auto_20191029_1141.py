# Generated by Django 2.2.6 on 2019-10-29 11:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipe_blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='description',
            field=models.TextField(blank=True, unique=True),
        ),
    ]

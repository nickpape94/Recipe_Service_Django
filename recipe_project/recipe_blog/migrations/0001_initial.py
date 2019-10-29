# Generated by Django 2.2.6 on 2019-10-29 13:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, default='no_photo.jpg', upload_to='media/recipe_pics')),
                ('recipe', models.CharField(max_length=200)),
                ('description', models.CharField(max_length=200)),
                ('cuisine', models.CharField(choices=[('African', 'AFRICAN'), ('American', 'AMERICAN'), ('British', 'BRITISH'), ('Caribbean', 'CARIBBEAN'), ('Chinese', 'CHINESE'), ('Other', 'OTHER')], default='Other', max_length=50)),
                ('ingredients', models.TextField(unique=True)),
                ('method', models.TextField(unique=True)),
                ('date_posted', models.DateTimeField(default=django.utils.timezone.now)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]

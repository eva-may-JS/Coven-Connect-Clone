# Generated by Django 4.2.16 on 2024-12-04 14:47

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, unique=True)),
                ('slug', models.SlugField(max_length=200, unique=True)),
                ('category', models.CharField(max_length=200)),
                ('date', models.DateTimeField()),
                ('time', models.DateTimeField()),
                ('location', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('familiar', models.IntegerField(choices=[(0, 'Yes'), (1, 'No')], default=0)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('status', models.IntegerField(choices=[(0, 'Draft'), (1, 'Published')], default=0)),
                ('excerpt', models.TextField()),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='event_posts', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
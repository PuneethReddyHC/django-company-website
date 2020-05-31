# Generated by Django 2.2.11 on 2020-05-20 16:27

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import mdeditor.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='MeanList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='menu name')),
                ('link', models.CharField(blank=True, max_length=100, null=True, verbose_name='Menu Link')),
                ('icon', models.CharField(blank=True, max_length=100, null=True, verbose_name='menu icon')),
                ('status', models.CharField(choices=[('y', 'Show'), ('n', 'Hide')], default='y', max_length=1, verbose_name='Display status')),
            ],
            options={
                'verbose_name': 'Menu Bar',
                'verbose_name_plural': 'Menu Bar',
            },
        ),
        migrations.CreateModel(
            name='Portfolio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, unique=True, verbose_name='Title')),
                ('slug', models.SlugField(max_length=200, unique=True, verbose_name='Slug')),
                ('excerpt', models.CharField(blank=True, max_length=200, verbose_name='Summary')),
                ('content', mdeditor.fields.MDTextField(verbose_name='content')),
                ('cover', models.ImageField(blank=True, upload_to='portfolio', verbose_name='Upload cover')),
                ('created_time', models.DateTimeField(auto_now=True, verbose_name='Creation time')),
                ('modified_time', models.DateTimeField(auto_now=True, verbose_name='Modified time')),
                ('views', models.PositiveIntegerField(default=0, verbose_name='Views')),
                ('words', models.PositiveIntegerField(default=0, verbose_name='Word count')),
                ('status', models.CharField(choices=[('p', 'Article Page'), ('c', 'Tutorial page'), ('d', 'Draft Box'), ('r', 'Recycle Bin')], default='p', max_length=1, verbose_name='Article status')),
                ('stick', models.CharField(choices=[('y', 'Sticky'), ('n', 'Do not top')], default='n', max_length=1, verbose_name='Whether sticky')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Author')),
            ],
            options={
                'verbose_name': 'Add Portfolio',
                'verbose_name_plural': 'Add Portfolio',
                'ordering': ['-created_time'],
            },
        ),
        migrations.CreateModel(
            name='Messages',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='leave me a message')),
                ('admin', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Webmaster')),
            ],
            options={
                'verbose_name': 'Website message',
                'verbose_name_plural': 'Website message',
            },
        ),
    ]
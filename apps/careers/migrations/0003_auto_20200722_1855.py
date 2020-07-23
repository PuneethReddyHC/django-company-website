# Generated by Django 2.2.11 on 2020-07-22 13:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('careers', '0002_auto_20200721_1616'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='status',
            field=models.CharField(choices=[('p', 'Published'), ('d', 'Draft Box'), ('r', 'Recycle Bin')], default='p', max_length=1, verbose_name='Job status'),
        ),
    ]
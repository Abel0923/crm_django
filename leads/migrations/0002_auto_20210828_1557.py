# Generated by Django 3.1.4 on 2021-08-28 12:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('leads', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='agent',
            name='first_name',
        ),
        migrations.RemoveField(
            model_name='agent',
            name='last_name',
        ),
        migrations.AlterField(
            model_name='lead',
            name='age',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='user',
            name='first_name',
            field=models.CharField(blank=True, max_length=150, verbose_name='first name'),
        ),
    ]
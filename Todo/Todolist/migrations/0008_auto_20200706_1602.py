# Generated by Django 3.0.5 on 2020-07-06 13:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Todolist', '0007_auto_20200706_1556'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='written',
            name='todo',
        ),
        migrations.AddField(
            model_name='written',
            name='content',
            field=models.CharField(default='ABC', max_length=50),
        ),
    ]

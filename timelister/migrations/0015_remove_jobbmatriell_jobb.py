# Generated by Django 2.2.1 on 2019-05-09 17:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('timelister', '0014_auto_20190509_1917'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='jobbmatriell',
            name='jobb',
        ),
    ]
# Generated by Django 2.2.1 on 2019-05-07 20:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('timelister', '0007_jobber_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jobber',
            name='beskrivelse',
            field=models.TextField(blank=True),
        ),
    ]

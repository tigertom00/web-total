# Generated by Django 2.2.1 on 2019-05-16 21:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testing', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='testimg',
            name='img',
            field=models.ImageField(upload_to='testing'),
        ),
    ]

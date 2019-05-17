# Generated by Django 2.2.1 on 2019-05-16 21:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TestImg',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
                ('img', models.ImageField(upload_to='jobb_profile_image')),
            ],
            options={
                'verbose_name': 'TestImg',
                'verbose_name_plural': 'TestImgs',
            },
        ),
    ]

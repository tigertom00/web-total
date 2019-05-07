# Generated by Django 2.2.1 on 2019-05-02 20:33

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
            name='GetTimeliste',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ordre_nr', models.PositiveSmallIntegerField(max_length=4, null=True)),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('date_timer', models.DateField(blank=True, null=True)),
                ('title', models.CharField(blank=True, max_length=64)),
                ('description', models.CharField(blank=True, max_length=256)),
                ('matriell', models.CharField(blank=True, max_length=256)),
                ('timer', models.SmallIntegerField(max_length=2, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]

# Generated by Django 2.2.1 on 2019-05-09 17:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('timelister', '0016_remove_jobber_matriell'),
    ]

    operations = [
        migrations.AddField(
            model_name='jobber',
            name='matriell',
            field=models.ManyToManyField(blank=True, to='timelister.JobbMatriell'),
        ),
        migrations.AddField(
            model_name='jobbmatriell',
            name='jobb',
            field=models.ForeignKey(default=1111, on_delete=django.db.models.deletion.CASCADE, to='timelister.Jobber'),
            preserve_default=False,
        ),
    ]

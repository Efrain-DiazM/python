# Generated by Django 4.1.2 on 2022-10-22 16:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_turista'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='project',
        ),
        migrations.RemoveField(
            model_name='turista',
            name='tiempoEstadia',
        ),
        migrations.AddField(
            model_name='turista',
            name='fechaLlegada',
            field=models.DateTimeField(null=True),
        ),
        migrations.DeleteModel(
            name='Project',
        ),
        migrations.DeleteModel(
            name='Task',
        ),
    ]

# Generated by Django 3.2.18 on 2023-04-27 04:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0012_auto_20230425_2213'),
    ]

    operations = [
        migrations.AddField(
            model_name='crearcurso',
            name='profesorCurso',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='myapp.usercourse'),
            preserve_default=False,
        ),
    ]

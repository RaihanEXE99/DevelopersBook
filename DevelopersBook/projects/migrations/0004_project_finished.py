# Generated by Django 3.0.6 on 2020-07-20 20:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0003_project_createdat'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='Finished',
            field=models.BooleanField(default=False),
        ),
    ]

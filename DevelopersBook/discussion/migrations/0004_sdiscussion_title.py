# Generated by Django 3.0.6 on 2020-07-24 10:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('discussion', '0003_auto_20200724_1601'),
    ]

    operations = [
        migrations.AddField(
            model_name='sdiscussion',
            name='title',
            field=models.TextField(default=None, max_length=70),
        ),
    ]

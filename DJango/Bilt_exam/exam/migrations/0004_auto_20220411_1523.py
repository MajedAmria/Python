# Generated by Django 2.2.4 on 2022-04-11 12:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exam', '0003_auto_20220411_1143'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='year',
            field=models.IntegerField(),
        ),
    ]

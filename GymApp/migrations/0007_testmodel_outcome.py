# Generated by Django 4.1.4 on 2022-12-30 14:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('GymApp', '0006_testmodel_height_testmodel_weight'),
    ]

    operations = [
        migrations.AddField(
            model_name='testmodel',
            name='Outcome',
            field=models.CharField(blank=True, max_length=30),
        ),
    ]

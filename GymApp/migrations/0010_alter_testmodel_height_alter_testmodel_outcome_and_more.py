# Generated by Django 4.1.4 on 2023-01-02 09:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('GymApp', '0009_testmodel_activity'),
    ]

    operations = [
        migrations.AlterField(
            model_name='testmodel',
            name='Height',
            field=models.IntegerField(blank=True, max_length=30),
        ),
        migrations.AlterField(
            model_name='testmodel',
            name='Outcome',
            field=models.IntegerField(blank=True, max_length=30),
        ),
        migrations.AlterField(
            model_name='testmodel',
            name='Weight',
            field=models.IntegerField(blank=True, max_length=30),
        ),
    ]

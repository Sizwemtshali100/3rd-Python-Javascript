# Generated by Django 4.1.4 on 2023-01-02 11:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('GymApp', '0011_alter_testmodel_height_alter_testmodel_outcome_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='testmodel',
            name='Height',
            field=models.CharField(blank=True, max_length=30),
        ),
        migrations.AlterField(
            model_name='testmodel',
            name='Outcome',
            field=models.CharField(blank=True, max_length=30),
        ),
        migrations.AlterField(
            model_name='testmodel',
            name='Weight',
            field=models.CharField(blank=True, max_length=30),
        ),
    ]
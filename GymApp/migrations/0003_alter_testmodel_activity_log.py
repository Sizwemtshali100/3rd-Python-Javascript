# Generated by Django 4.1.4 on 2022-12-30 13:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('GymApp', '0002_testmodel_activity_log_testmodel_gender_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='testmodel',
            name='Activity_log',
            field=models.CharField(choices=[('Active', 'Active'), ('Not Active', 'Not Active')], default=False, max_length=10),
        ),
    ]

# Generated by Django 3.2.16 on 2023-04-04 14:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cinema', '0004_alter_cinemahall_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cinemahall',
            name='name',
            field=models.CharField(max_length=255),
        ),
    ]
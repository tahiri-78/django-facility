# Generated by Django 4.1.3 on 2022-11-23 12:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('operation', '0001_initial'),
        ('fichier', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='fichier',
            name='operation',
            field=models.ManyToManyField(to='operation.operation'),
        ),
    ]

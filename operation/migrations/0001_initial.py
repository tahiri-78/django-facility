# Generated by Django 4.1.3 on 2022-11-23 11:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='operation',
            fields=[
                ('id_op', models.AutoField(primary_key=True, serialize=False)),
                ('nom_operation', models.CharField(max_length=10)),
                ('object', models.IntegerField(max_length=10)),
                ('theme', models.CharField(max_length=100)),
                ('date_creation', models.DateTimeField(auto_now_add=True)),
                ('date_modification', models.DateTimeField(auto_now=True)),
                ('client_op', models.CharField(max_length=20)),
                ('entete', models.CharField(max_length=900)),
            ],
        ),
    ]
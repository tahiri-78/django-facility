# Generated by Django 4.1.3 on 2022-11-23 12:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('operation', '0001_initial'),
        ('lots', '0002_lots_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='lots',
            name='operation',
            field=models.ForeignKey(default=220224, on_delete=django.db.models.deletion.DO_NOTHING, to='operation.operation'),
            preserve_default=False,
        ),
    ]

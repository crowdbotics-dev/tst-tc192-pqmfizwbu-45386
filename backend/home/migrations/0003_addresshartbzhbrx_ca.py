# Generated by Django 2.2.28 on 2022-11-18 08:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_addresshartbzhbrx'),
    ]

    operations = [
        migrations.AddField(
            model_name='addresshartbzhbrx',
            name='ca',
            field=models.BigIntegerField(blank=True, null=True),
        ),
    ]

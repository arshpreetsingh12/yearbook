# Generated by Django 2.2.5 on 2019-10-05 20:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('yearapp', '0013_auto_20191004_0717'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='phone',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
    ]

# Generated by Django 2.2.5 on 2019-10-08 06:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('yearapp', '0034_auto_20191008_0609'),
    ]

    operations = [
        migrations.AlterField(
            model_name='invitation',
            name='address',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]

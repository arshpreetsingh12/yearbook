# Generated by Django 2.2.5 on 2019-10-07 06:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('yearapp', '0019_remove_profile_phone'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='phone',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
    ]

# Generated by Django 2.2.5 on 2019-10-07 05:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('yearapp', '0016_auto_20191007_0558'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='paypal_email',
            field=models.EmailField(blank=True, max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='phone',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]

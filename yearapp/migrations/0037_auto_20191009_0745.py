# Generated by Django 2.2.5 on 2019-10-09 07:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('yearapp', '0036_auto_20191008_0630'),
    ]

    operations = [
        migrations.AlterField(
            model_name='invitation',
            name='address',
            field=models.TextField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='invitation',
            name='website',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='address',
            field=models.TextField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='billing_address',
            field=models.TextField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='company_name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='paypal_email',
            field=models.EmailField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='website',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='setevent',
            name='description',
            field=models.TextField(blank=True, max_length=200, null=True),
        ),
    ]

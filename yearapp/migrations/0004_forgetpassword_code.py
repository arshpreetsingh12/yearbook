# Generated by Django 2.2.5 on 2019-09-26 07:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('yearapp', '0003_auto_20190926_0440'),
    ]

    operations = [
        migrations.AddField(
            model_name='forgetpassword',
            name='code',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Code'),
        ),
    ]

# Generated by Django 2.2.5 on 2019-10-11 04:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('yearapp', '0049_auto_20191010_1310'),
    ]

    operations = [
        migrations.AlterField(
            model_name='setevent',
            name='posting',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='yearapp.Posting', verbose_name='Posting'),
        ),
    ]

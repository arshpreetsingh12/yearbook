# Generated by Django 2.2.5 on 2019-10-10 11:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('yearapp', '0042_invitation_setevent'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='setevent',
            name='user',
        ),
        migrations.DeleteModel(
            name='Invitation',
        ),
        migrations.DeleteModel(
            name='SetEvent',
        ),
    ]

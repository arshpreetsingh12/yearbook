# Generated by Django 2.2.5 on 2019-10-10 13:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('yearapp', '0048_auto_20191010_1309'),
    ]

    operations = [
        migrations.RenameField(
            model_name='sellerinformation',
            old_name='seller_country',
            new_name='country',
        ),
        migrations.RenameField(
            model_name='sellerinformation',
            old_name='seller_state',
            new_name='state',
        ),
    ]

# Generated by Django 2.2.5 on 2019-10-11 12:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('yearapp', '0058_generaladmissionseat'),
    ]

    operations = [
        migrations.RenameField(
            model_name='generaladmissionseat',
            old_name='bronze_availability',
            new_name='bronze_seat_availability',
        ),
        migrations.RenameField(
            model_name='generaladmissionseat',
            old_name='bronze_price',
            new_name='bronze_seat_price',
        ),
        migrations.RenameField(
            model_name='generaladmissionseat',
            old_name='gold_availability',
            new_name='gold_seat_availability',
        ),
        migrations.RenameField(
            model_name='generaladmissionseat',
            old_name='gold_price',
            new_name='gold_seat_price',
        ),
        migrations.RenameField(
            model_name='generaladmissionseat',
            old_name='silver_availability',
            new_name='silver_seat_availability',
        ),
        migrations.RenameField(
            model_name='generaladmissionseat',
            old_name='silver_price',
            new_name='silver_seat_price',
        ),
    ]

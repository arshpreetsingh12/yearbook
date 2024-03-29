# Generated by Django 2.2.5 on 2019-10-11 10:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('yearapp', '0057_auto_20191011_0920'),
    ]

    operations = [
        migrations.CreateModel(
            name='GeneralAdmissionSeat',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gold_seat', models.CharField(blank=True, max_length=15, null=True)),
                ('gold_availability', models.CharField(blank=True, max_length=5, null=True)),
                ('gold_price', models.CharField(blank=True, max_length=5, null=True)),
                ('gold_is_enable', models.BooleanField(blank=True, default=False, null=True)),
                ('silver_seat', models.CharField(blank=True, max_length=15, null=True)),
                ('silver_availability', models.CharField(blank=True, max_length=5, null=True)),
                ('silver_price', models.CharField(blank=True, max_length=5, null=True)),
                ('silver_is_enable', models.BooleanField(blank=True, default=False, null=True)),
                ('bronze_seat', models.CharField(blank=True, max_length=15, null=True)),
                ('bronze_availability', models.CharField(blank=True, max_length=5, null=True)),
                ('bronze_price', models.CharField(blank=True, max_length=5, null=True)),
                ('bronze_is_enable', models.BooleanField(blank=True, default=False, null=True)),
                ('posting', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='yearapp.Posting', verbose_name='Posting')),
            ],
        ),
    ]

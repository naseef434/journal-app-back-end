# Generated by Django 4.0 on 2021-12-16 14:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_debit_credit'),
    ]

    operations = [
        migrations.AddField(
            model_name='credit',
            name='credit',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='debit',
            name='credit',
            field=models.IntegerField(default=0),
        ),
    ]

# Generated by Django 4.0 on 2021-12-16 12:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_journalentry'),
    ]

    operations = [
        migrations.CreateModel(
            name='Debit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('account', models.IntegerField()),
                ('debit', models.IntegerField(default=0)),
                ('discription', models.CharField(max_length=100)),
                ('journalEntry_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.journalentry')),
            ],
        ),
        migrations.CreateModel(
            name='Credit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('account', models.IntegerField()),
                ('debit', models.IntegerField(default=0)),
                ('discription', models.CharField(max_length=100)),
                ('journalEntry_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.journalentry')),
            ],
        ),
    ]
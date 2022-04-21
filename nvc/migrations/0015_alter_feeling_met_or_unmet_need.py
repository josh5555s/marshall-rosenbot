# Generated by Django 3.2.8 on 2022-01-01 02:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nvc', '0014_feeling_met_or_unmet_need'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feeling',
            name='met_or_unmet_need',
            field=models.CharField(choices=[('m', 'Met'), ('u', 'Unmet'), ('b', 'Both')], default='u', max_length=1),
        ),
    ]
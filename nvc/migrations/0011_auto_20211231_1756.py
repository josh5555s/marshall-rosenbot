# Generated by Django 3.2.8 on 2022-01-01 01:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nvc', '0010_needpoem'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='feelingpoem',
            options={'ordering': ['title']},
        ),
        migrations.AlterModelOptions(
            name='needpoem',
            options={'ordering': ['title']},
        ),
        migrations.AddField(
            model_name='feeling',
            name='status',
            field=models.CharField(choices=[('m', 'Met'), ('u', 'Unmet'), ('b', 'Both')], default='u', max_length=1),
        ),
    ]

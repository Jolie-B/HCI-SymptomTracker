# Generated by Django 4.1.3 on 2022-11-20 23:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0005_alter_day_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='day',
            name='date',
            field=models.CharField(max_length=10, unique=True),
        ),
    ]
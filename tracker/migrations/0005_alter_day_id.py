# Generated by Django 4.1.3 on 2022-11-20 21:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0004_alter_day_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='day',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]

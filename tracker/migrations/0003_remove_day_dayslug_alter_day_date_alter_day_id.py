# Generated by Django 4.1.3 on 2022-11-20 20:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0002_day_id_alter_day_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='day',
            name='daySlug',
        ),
        migrations.AlterField(
            model_name='day',
            name='date',
            field=models.CharField(max_length=6),
        ),
        migrations.AlterField(
            model_name='day',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]

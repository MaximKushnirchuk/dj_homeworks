# Generated by Django 3.1.2 on 2023-11-23 20:30

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("measurement", "0004_auto_20231123_2029"),
    ]

    operations = [
        migrations.AlterField(
            model_name="measurement",
            name="temperature",
            field=models.FloatField(verbose_name="температура"),
        ),
    ]

# Generated by Django 3.1.2 on 2023-11-23 20:29

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("measurement", "0003_auto_20231123_2028"),
    ]

    operations = [
        migrations.AlterField(
            model_name="measurement",
            name="temperature",
            field=models.DecimalField(
                decimal_places=2, max_digits=6, verbose_name="температура"
            ),
        ),
    ]
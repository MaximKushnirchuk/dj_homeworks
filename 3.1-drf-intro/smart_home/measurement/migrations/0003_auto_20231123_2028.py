# Generated by Django 3.1.2 on 2023-11-23 20:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("measurement", "0002_auto_20231123_1428"),
    ]

    operations = [
        migrations.AlterField(
            model_name="measurement",
            name="sensor",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="measurements",
                to="measurement.sensor",
            ),
        ),
        migrations.AlterField(
            model_name="measurement",
            name="temperature",
            field=models.DecimalField(
                decimal_places=2, max_digits=3, verbose_name="температура"
            ),
        ),
    ]
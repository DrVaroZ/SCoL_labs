# Generated by Django 4.2.1 on 2023-09-14 07:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("car_rent", "0011_worker"),
    ]

    operations = [
        migrations.CreateModel(
            name="Vacancy",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("position", models.CharField(max_length=100)),
                ("position_info", models.TextField()),
                ("salary", models.IntegerField()),
            ],
        ),
    ]

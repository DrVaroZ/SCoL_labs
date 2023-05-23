# Generated by Django 4.2.1 on 2023-05-22 21:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Brand",
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
                (
                    "name",
                    models.CharField(
                        help_text="Enter a auto brand (e.g. Toyota, Ford etc.)",
                        max_length=30,
                        verbose_name="Brand",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Car",
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
                (
                    "release_year",
                    models.IntegerField(max_length=4, verbose_name="Release year"),
                ),
                ("cost", models.IntegerField(max_length=9, verbose_name="Cost")),
                (
                    "rent_per_day",
                    models.IntegerField(max_length=6, verbose_name="Rent per day"),
                ),
                (
                    "brand",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="car_rent.brand",
                    ),
                ),
            ],
            options={"ordering": ["release_year"],},
        ),
        migrations.CreateModel(
            name="CarModel",
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
                (
                    "name",
                    models.CharField(
                        help_text="Enter a auto model (sedan, hatchback, lift back, crossover etc.)",
                        max_length=30,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Client",
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
                (
                    "first_name",
                    models.CharField(help_text="Enter your first name", max_length=100),
                ),
                (
                    "last_name",
                    models.CharField(help_text="Enter your last name", max_length=100),
                ),
                ("date_birthday", models.DateField(help_text="Enter your birthday")),
                (
                    "email",
                    models.EmailField(help_text="Enter your email", max_length=254),
                ),
                (
                    "phone_number",
                    models.CharField(
                        help_text="Enter your phone number", max_length=20
                    ),
                ),
                ("number_of_rents", models.PositiveIntegerField(max_length=5)),
            ],
        ),
        migrations.CreateModel(
            name="Discount",
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
                (
                    "name",
                    models.CharField(
                        help_text="Name of the discount (bronze, silver, gold, platinum)",
                        max_length=15,
                    ),
                ),
                ("percentage", models.PositiveIntegerField(max_length=2)),
            ],
        ),
        migrations.CreateModel(
            name="Fine",
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
                (
                    "name",
                    models.CharField(
                        help_text="Name of the fine: parking in inappropriate place, car damage etc",
                        max_length=30,
                    ),
                ),
                ("sum_fine", models.IntegerField(max_length=4)),
            ],
        ),
        migrations.CreateModel(
            name="Rent",
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
                ("start_date", models.DateField(blank=True, null=True)),
                ("finish_date", models.DateField(blank=True, null=True)),
                ("amount_of_rent_days", models.IntegerField(default=1, max_length=3)),
                ("rent_cost", models.IntegerField(max_length=6)),
                ("discount_sum", models.IntegerField(max_length=6)),
                ("fine_sum", models.IntegerField(max_length=4)),
                ("result_sum", models.IntegerField(max_length=6)),
                (
                    "status",
                    models.CharField(
                        blank=True,
                        choices=[
                            ("m", "Maintenance"),
                            ("o", "On rent"),
                            ("a", "Available"),
                            ("r", "Reserved"),
                        ],
                        default="m",
                        help_text="Car availability",
                        max_length=1,
                    ),
                ),
                (
                    "car",
                    models.OneToOneField(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="car_rent.car",
                    ),
                ),
                (
                    "client",
                    models.OneToOneField(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="car_rent.client",
                    ),
                ),
            ],
            options={"ordering": ["start_date"],},
        ),
        migrations.AddField(
            model_name="client",
            name="discount",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="car_rent.discount",
            ),
        ),
        migrations.AddField(
            model_name="client",
            name="fines",
            field=models.ForeignKey(
                blank=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="car_rent.fine",
            ),
        ),
        migrations.AddField(
            model_name="car",
            name="car_model",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="car_rent.carmodel",
            ),
        ),
    ]

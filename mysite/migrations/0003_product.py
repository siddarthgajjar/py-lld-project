# Generated by Django 5.2.dev20241023172036 on 2024-10-29 05:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("mysite", "0002_user_address"),
    ]

    operations = [
        migrations.CreateModel(
            name="Product",
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
                ("name", models.CharField(max_length=50)),
                ("price", models.FloatField()),
                ("description", models.CharField(max_length=255)),
                ("stock", models.IntegerField()),
            ],
        ),
    ]

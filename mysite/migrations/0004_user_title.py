# Generated by Django 5.2.dev20241023172036 on 2024-10-29 05:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("mysite", "0003_product"),
    ]

    operations = [
        migrations.AddField(
            model_name="user",
            name="title",
            field=models.CharField(
                choices=[
                    ("Mr", "Mr"),
                    ("Mrs", "Mrs"),
                    ("Miss", "Miss"),
                    ("Dr", "Dr"),
                    ("Prof", "Prof"),
                ],
                null=True,
            ),
        ),
    ]
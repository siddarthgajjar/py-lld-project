# Generated by Django 5.2.dev20241023172036 on 2024-10-29 04:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("mysite", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="user",
            name="address",
            field=models.CharField(max_length=255, null=True),
        ),
    ]

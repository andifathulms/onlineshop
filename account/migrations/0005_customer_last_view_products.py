# Generated by Django 4.1.3 on 2022-12-17 05:39

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("account", "0004_alter_customer_account"),
    ]

    operations = [
        migrations.AddField(
            model_name="customer",
            name="last_view_products",
            field=django.contrib.postgres.fields.ArrayField(
                base_field=models.PositiveIntegerField(),
                default=[0, 0, 0, 0, 0],
                size=None,
            ),
        ),
    ]

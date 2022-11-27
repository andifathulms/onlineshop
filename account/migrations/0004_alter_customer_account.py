# Generated by Django 4.1.3 on 2022-11-26 05:10

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("account", "0003_rename_adress_address_rename_adress_address_address"),
    ]

    operations = [
        migrations.AlterField(
            model_name="customer",
            name="account",
            field=models.OneToOneField(
                on_delete=django.db.models.deletion.CASCADE,
                primary_key=True,
                related_name="user_customer",
                serialize=False,
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]

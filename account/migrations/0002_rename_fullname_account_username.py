# Generated by Django 4.1.3 on 2022-11-24 07:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("account", "0001_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="account", old_name="fullname", new_name="username",
        ),
    ]
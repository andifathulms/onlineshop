# Generated by Django 4.1.3 on 2022-11-26 05:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("product", "0002_color_size_product"),
    ]

    operations = [
        migrations.AlterField(
            model_name="color", name="name", field=models.CharField(max_length=20),
        ),
    ]

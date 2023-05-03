# Generated by Django 4.2 on 2023-04-25 00:57

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("users", "0012_remove_products_drinks_remove_products_foods"),
    ]

    operations = [
        migrations.AddField(
            model_name="products",
            name="drinks",
            field=models.JSONField(blank=True, default=list, null=True),
        ),
        migrations.AddField(
            model_name="products",
            name="foods",
            field=models.JSONField(blank=True, default=list, null=True),
        ),
    ]

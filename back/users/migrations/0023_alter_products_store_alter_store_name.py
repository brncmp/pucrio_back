# Generated by Django 4.2 on 2023-05-01 23:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("users", "0022_alter_store_owner"),
    ]

    operations = [
        migrations.AlterField(
            model_name="products",
            name="store",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to="users.store",
                to_field="name",
            ),
        ),
        migrations.AlterField(
            model_name="store",
            name="name",
            field=models.CharField(max_length=255, unique=True),
        ),
    ]

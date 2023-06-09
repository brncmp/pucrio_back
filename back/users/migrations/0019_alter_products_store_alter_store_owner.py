# Generated by Django 4.2 on 2023-04-28 00:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("users", "0018_alter_products_store_alter_store_owner"),
    ]

    operations = [
        migrations.AlterField(
            model_name="products",
            name="store",
            field=models.ForeignKey(
                db_column="name",
                on_delete=django.db.models.deletion.CASCADE,
                to="users.store",
            ),
        ),
        migrations.AlterField(
            model_name="store",
            name="owner",
            field=models.ForeignKey(
                db_column="first_name",
                on_delete=django.db.models.deletion.CASCADE,
                to="users.users",
            ),
        ),
    ]

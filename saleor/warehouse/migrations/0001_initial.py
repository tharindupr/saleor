# Generated by Django 2.2.6 on 2019-11-13 13:08

import uuid

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("shipping", "0017_django_price_2"),
        ("account", "0034_service_account_token"),
    ]

    operations = [
        migrations.CreateModel(
            name="Warehouse",
            fields=[
                (
                    "uuid",
                    models.UUIDField(
                        default=uuid.uuid4, primary_key=True, serialize=False
                    ),
                ),
                (
                    "name",
                    models.CharField(max_length=50, verbose_name="Warehouse name"),
                ),
                (
                    "company_name",
                    models.CharField(max_length=100, verbose_name="Legal company name"),
                ),
                (
                    "email",
                    models.EmailField(
                        blank=True,
                        default="",
                        max_length=254,
                        verbose_name="Email address",
                    ),
                ),
                (
                    "address",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="account.Address",
                    ),
                ),
                (
                    "shipping_zones",
                    models.ManyToManyField(blank=True, to="shipping.ShippingZone"),
                ),
            ],
            options={
                "ordering": ("-name",),
                "permissions": (("manage_warehouses", "Manage warehouses."),),
            },
        )
    ]

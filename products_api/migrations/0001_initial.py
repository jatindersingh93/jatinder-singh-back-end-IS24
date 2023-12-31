# Generated by Django 3.1.12 on 2023-07-11 14:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ProductsModel',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('product_id', models.IntegerField(null=True, unique=True)),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField(blank=True, null=True)),
                ('colour', models.CharField(blank=True, max_length=100, null=True)),
                ('size', models.PositiveSmallIntegerField(blank=True, choices=[(1, 'Small'), (2, 'Medium'), (3, 'Large')], null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'db_table': 'products',
            },
        ),
    ]

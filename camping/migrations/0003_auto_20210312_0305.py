# Generated by Django 3.1.6 on 2021-03-11 22:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('camping', '0002_carpas_precio'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carpas',
            name='precio',
            field=models.DecimalField(blank=True, decimal_places=2, default=60000, max_digits=10, null=True),
        ),
    ]

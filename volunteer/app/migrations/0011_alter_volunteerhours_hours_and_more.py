# Generated by Django 5.0.7 on 2024-07-24 20:01

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0010_rename_date_volunteerhours_date_from_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='volunteerhours',
            name='hours',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True),
        ),
        migrations.AlterField(
            model_name='volunteerhours',
            name='organization',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.organization'),
        ),
    ]

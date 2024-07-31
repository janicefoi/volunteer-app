# Generated by Django 5.0.7 on 2024-07-25 09:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0014_remove_donation_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='donation',
            name='funds_raised',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='donation',
            name='goal',
            field=models.PositiveIntegerField(),
        ),
    ]
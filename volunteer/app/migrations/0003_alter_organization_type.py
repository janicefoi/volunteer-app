# Generated by Django 5.0.7 on 2024-07-15 18:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_organization_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='organization',
            name='type',
            field=models.CharField(choices=[('Elderly Homes', 'Elderly Homes'), ('Hospitals & Clinics', 'Hospitals & Clinics'), ('Children Homes', 'Children Homes')], max_length=25),
        ),
    ]

# Generated by Django 4.2.9 on 2024-02-26 17:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tripapp', '0002_team'),
    ]

    operations = [
        migrations.AlterField(
            model_name='team',
            name='img',
            field=models.ImageField(upload_to='pics1'),
        ),
    ]

# Generated by Django 3.2.23 on 2024-01-18 09:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobportal', '0007_auto_20240108_1518'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='salary',
            field=models.IntegerField(null=True),
        ),
    ]

# Generated by Django 3.2.23 on 2023-12-22 16:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='agency',
            fields=[
                ('agency_id', models.IntegerField(primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=30, null=True)),
                ('email', models.EmailField(max_length=30, null=True)),
                ('address', models.CharField(max_length=100, null=True)),
                ('gender', models.CharField(max_length=30)),
                ('phone', models.IntegerField(null=True)),
                ('password', models.CharField(max_length=30, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='job',
            fields=[
                ('job_id', models.IntegerField(primary_key=True, serialize=False)),
                ('job', models.CharField(max_length=30, null=True)),
                ('location', models.CharField(max_length=40, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='login1',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=30, null=True)),
                ('password', models.IntegerField(null=True)),
                ('usertype', models.IntegerField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('username', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=30, null=True)),
                ('address', models.CharField(max_length=100, null=True)),
                ('gender', models.CharField(max_length=30, null=True)),
                ('phone', models.IntegerField(null=True)),
                ('qualification', models.CharField(max_length=30, null=True)),
                ('resume', models.FileField(null=True, upload_to='')),
                ('password', models.CharField(max_length=20, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='application',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(null=True)),
                ('job_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='jobportal.job')),
                ('std_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='jobportal.student')),
            ],
        ),
    ]
# Generated by Django 5.0.4 on 2024-05-09 11:34

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0003_alter_job_company_delete_company'),
        ('signup', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Application',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('street_name', models.CharField(max_length=200)),
                ('house_number', models.IntegerField()),
                ('city', models.CharField(max_length=200)),
                ('country', models.CharField(max_length=200)),
                ('postal', models.IntegerField()),
                ('cover_letter', models.FileField(upload_to='')),
                ('job', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='jobs.job')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='signup.individual')),
            ],
            options={
                'unique_together': {('user', 'job')},
            },
        ),
        migrations.CreateModel(
            name='Experiences',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('workplace', models.CharField(max_length=200)),
                ('role', models.CharField(max_length=300)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('application', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='jobs.application')),
            ],
        ),
        migrations.CreateModel(
            name='References',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('phone_number', models.IntegerField()),
                ('email', models.CharField(max_length=200)),
                ('contact_bool', models.BooleanField()),
                ('application', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='jobs.application')),
            ],
        ),
    ]

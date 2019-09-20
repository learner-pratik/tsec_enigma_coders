# Generated by Django 2.1.7 on 2019-09-20 07:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Victim',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Victim_name', models.CharField(max_length=200)),
                ('Victim_address', models.CharField(max_length=200)),
                ('Victim_number', models.CharField(max_length=10)),
                ('Victim_email', models.CharField(max_length=200)),
                ('Victim_pass', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Volunteer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Volunteer_name', models.CharField(max_length=200)),
                ('Volunteer_address', models.CharField(max_length=200)),
                ('Volunteer_number', models.CharField(max_length=10)),
                ('Volunteer_email', models.CharField(max_length=200)),
                ('Volunteer_pass', models.CharField(max_length=200)),
                ('Volunteer_designation', models.CharField(max_length=200)),
                ('Volunteer_maxcapacity', models.IntegerField(default=0)),
            ],
        ),
    ]
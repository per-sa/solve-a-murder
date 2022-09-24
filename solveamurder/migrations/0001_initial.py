# Generated by Django 4.1.1 on 2022-09-24 15:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Suspect',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('date_of_birth', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Victim',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('date_of_birth', models.DateField()),
                ('city_country', models.CharField(max_length=100)),
                ('date_of_death', models.DateField()),
                ('cause_of_death', models.CharField(max_length=100)),
                ('main_suspect', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='solveamurder.suspect')),
            ],
        ),
        migrations.CreateModel(
            name='Cases',
            fields=[
                ('case_id', models.AutoField(primary_key=True, serialize=False)),
                ('case_name', models.CharField(max_length=255)),
                ('case_date', models.DateTimeField()),
                ('case_description', models.TextField()),
                ('is_unsolved', models.BooleanField(default=True)),
                ('case_main_suspect', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='solveamurder.suspect')),
                ('case_victims', models.ManyToManyField(to='solveamurder.victim')),
            ],
        ),
    ]
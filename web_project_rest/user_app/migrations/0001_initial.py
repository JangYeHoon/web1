# Generated by Django 3.1.7 on 2021-03-17 01:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=40)),
                ('name_ko', models.CharField(max_length=20)),
                ('name_eng', models.CharField(max_length=20)),
                ('call', models.CharField(max_length=15)),
                ('passport', models.CharField(max_length=20)),
                ('country', models.CharField(max_length=30)),
                ('birthday', models.IntegerField()),
                ('sex', models.IntegerField()),
            ],
        ),
    ]

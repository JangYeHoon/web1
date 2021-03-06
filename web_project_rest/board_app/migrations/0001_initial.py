# Generated by Django 3.1.7 on 2021-03-17 07:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('user_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Board',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('board_name', models.CharField(max_length=30)),
                ('title', models.CharField(max_length=30)),
                ('read_count', models.IntegerField()),
                ('write_date', models.DateTimeField()),
                ('contents', models.TextField()),
                ('group', models.IntegerField()),
                ('depth', models.CharField(max_length=30)),
                ('board_writer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='board_writer', to='user_app.user')),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('write_time', models.DateTimeField()),
                ('contents', models.TextField()),
                ('c_list', models.IntegerField()),
                ('c_level', models.CharField(max_length=100)),
                ('board_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='board_id', to='board_app.board')),
                ('comment_writer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comment_writer', to='user_app.user')),
            ],
        ),
    ]

# Generated by Django 2.0.4 on 2019-02-22 16:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='cb',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cb_count', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='mb',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mb_count', models.IntegerField()),
            ],
        ),
    ]

# Generated by Django 2.2.5 on 2019-09-25 05:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('demo', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CalculateField',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('a', models.IntegerField()),
                ('b', models.IntegerField()),
            ],
        ),
    ]

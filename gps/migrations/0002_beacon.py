# Generated by Django 2.1.1 on 2018-11-06 10:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gps', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Beacon',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('beacon', models.CharField(max_length=20)),
                ('distance', models.FloatField(null=True)),
            ],
        ),
    ]

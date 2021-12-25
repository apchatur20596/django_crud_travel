# Generated by Django 4.0 on 2021-12-25 08:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TravelPlans',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('start', models.CharField(max_length=50)),
                ('end', models.CharField(max_length=50)),
                ('description', models.TextField()),
                ('price', models.IntegerField()),
            ],
        ),
    ]

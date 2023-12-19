# Generated by Django 4.2.8 on 2023-12-18 11:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='students',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=400)),
                ('college', models.CharField(max_length=400)),
                ('address', models.CharField(max_length=400)),
                ('age', models.IntegerField(max_length=3)),
                ('is_active', models.BooleanField(default=True)),
            ],
        ),
    ]

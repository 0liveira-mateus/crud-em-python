# Generated by Django 4.2.4 on 2023-08-01 23:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='carros',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Modelo', models.CharField(max_length=30)),
                ('Marca', models.CharField(max_length=30)),
                ('Ano', models.IntegerField()),
            ],
        ),
    ]

# Generated by Django 4.1.3 on 2024-04-10 06:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('city', models.CharField(max_length=150)),
                ('hobby', models.CharField(max_length=150)),
            ],
        ),
    ]

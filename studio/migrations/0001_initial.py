# Generated by Django 3.2.18 on 2023-05-11 18:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Offer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('expiration_date', models.DateField(null=True)),
            ],
        ),
    ]

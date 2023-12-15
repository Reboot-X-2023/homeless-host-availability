# Generated by Django 4.2.7 on 2023-11-28 08:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Guest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='Host',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='HostAvailability',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('guest', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='hha.guest')),
                ('host', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='hha.host')),
            ],
        ),
    ]
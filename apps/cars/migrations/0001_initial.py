# Generated by Django 4.2.6 on 2023-10-23 14:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auto_parks', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CarModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand', models.CharField(max_length=20)),
                ('year', models.IntegerField()),
                ('typeCar', models.CharField(max_length=12)),
                ('countPlace', models.IntegerField()),
                ('eugenie', models.FloatField()),
                ('auto_park', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cars', to='auto_parks.autoparkmodel')),
                ('update_at', models.DateTimeField(auto_now=True)),
                ('create_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'db_table': 'cars',
            },
        ),
    ]
# Generated by Django 5.1.5 on 2025-01-31 13:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_databs'),
    ]

    operations = [
        migrations.CreateModel(
            name='experience',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tahun', models.IntegerField()),
                ('posisi', models.CharField(max_length=50)),
                ('di', models.CharField(max_length=50)),
                ('kota', models.CharField(max_length=50)),
                ('cerita', models.CharField(max_length=200)),
                ('show', models.BooleanField()),
            ],
        ),
    ]

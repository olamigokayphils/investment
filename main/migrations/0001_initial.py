# Generated by Django 3.0 on 2021-05-11 07:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Investments',
            fields=[
                ('uid', models.AutoField(primary_key=True, serialize=False)),
                ('plan', models.CharField(max_length=1000)),
                ('amount', models.CharField(max_length=1000)),
                ('investor', models.CharField(max_length=1000)),
                ('phone', models.CharField(max_length=1000)),
                ('name', models.CharField(max_length=1000)),
                ('start', models.DateTimeField(auto_now_add=True)),
                ('end', models.DateTimeField()),
                ('status', models.CharField(choices=[('Pending', 'Pending'), ('Active', 'Active')], max_length=7)),
                ('unit', models.IntegerField()),
                ('address', models.CharField(max_length=1000)),
                ('fullname', models.CharField(max_length=1000)),
                ('day', models.CharField(blank=True, max_length=1000)),
                ('platform', models.CharField(blank=True, max_length=1000)),
            ],
            options={
                'verbose_name': 'Investment',
                'verbose_name_plural': 'Investments',
                'ordering': ('-plan',),
            },
        ),
    ]

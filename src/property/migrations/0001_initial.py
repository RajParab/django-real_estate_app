# Generated by Django 2.2.4 on 2019-08-18 06:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Property',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('area', models.DecimalField(decimal_places=2, max_digits=10)),
                ('types', models.CharField(choices=[('Rent', 'Rent'), ('Sale', 'Sale')], max_length=10)),
                ('bath', models.IntegerField()),
                ('bed', models.IntegerField()),
                ('garage', models.IntegerField()),
                ('created_on', models.TimeField(auto_now=True)),
                ('updated_on', models.TimeField(auto_now_add=True)),
            ],
        ),
    ]
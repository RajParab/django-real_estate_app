# Generated by Django 2.2.4 on 2019-08-18 11:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('contact_no', models.CharField(max_length=15)),
            ],
        ),
    ]

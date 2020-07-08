# Generated by Django 3.0.8 on 2020-07-06 01:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Snippet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=500)),
                ('language', models.CharField(max_length=255)),
                ('title', models.CharField(max_length=255)),
                ('description', models.CharField(max_length=500)),
                ('date_added', models.DateField(blank=True, null=True)),
            ],
        ),
    ]
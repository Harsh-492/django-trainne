# Generated by Django 4.2.14 on 2024-07-19 10:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0002_alter_myproject_technology'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myproject',
            name='end_date',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='myproject',
            name='start_date',
            field=models.DateTimeField(),
        ),
    ]
# Generated by Django 2.2.3 on 2019-10-13 13:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0007_storeevent'),
    ]

    operations = [
        migrations.AlterField(
            model_name='storeevent',
            name='event_date',
            field=models.DateField(),
        ),
    ]
# Generated by Django 3.1 on 2020-08-26 07:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='date_added',
            field=models.DateTimeField(auto_created=True, editable=False),
        ),
    ]
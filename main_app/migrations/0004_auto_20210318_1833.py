# Generated by Django 3.1.7 on 2021-03-18 18:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0003_auto_20210318_1822'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='review',
            options={'ordering': ['created_at']},
        ),
    ]
# Generated by Django 3.2.23 on 2023-12-21 12:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0014_auto_20231221_1237'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='edited_on',
        ),
    ]

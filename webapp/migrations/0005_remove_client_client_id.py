# Generated by Django 4.2 on 2023-04-16 10:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0004_alter_client_client_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='client',
            name='client_id',
        ),
    ]
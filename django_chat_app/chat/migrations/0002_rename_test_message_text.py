# Generated by Django 4.2.2 on 2023-07-03 11:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='message',
            old_name='test',
            new_name='text',
        ),
    ]
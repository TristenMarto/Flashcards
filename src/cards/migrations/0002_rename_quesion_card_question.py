# Generated by Django 3.2.14 on 2022-07-26 19:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cards', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='card',
            old_name='quesion',
            new_name='question',
        ),
    ]

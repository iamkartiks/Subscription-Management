# Generated by Django 3.2.2 on 2021-05-17 16:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_oreders_products'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Oreders',
            new_name='Orders',
        ),
    ]
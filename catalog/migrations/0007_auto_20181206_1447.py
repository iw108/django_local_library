# Generated by Django 2.1.4 on 2018-12-06 13:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0006_auto_20181206_1152'),
    ]

    operations = [
        migrations.RenameField(
            model_name='language',
            old_name='language',
            new_name='name',
        ),
    ]
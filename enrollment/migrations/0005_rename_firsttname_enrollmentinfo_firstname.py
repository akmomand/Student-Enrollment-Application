# Generated by Django 4.2 on 2024-04-23 16:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('enrollment', '0004_rename_studentname_enrollmentinfo_firsttname_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='enrollmentinfo',
            old_name='firsttname',
            new_name='firstname',
        ),
    ]

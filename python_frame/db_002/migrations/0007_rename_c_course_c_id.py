# Generated by Django 3.2.15 on 2022-09-13 18:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('db_002', '0006_rename_c_id_course_c'),
    ]

    operations = [
        migrations.RenameField(
            model_name='course',
            old_name='c',
            new_name='c_id',
        ),
    ]

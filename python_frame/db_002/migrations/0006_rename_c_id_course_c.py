# Generated by Django 3.2.15 on 2022-09-13 18:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('db_002', '0005_rename_a_id_student_a'),
    ]

    operations = [
        migrations.RenameField(
            model_name='course',
            old_name='c_id',
            new_name='c',
        ),
    ]
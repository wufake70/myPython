# Generated by Django 3.2.15 on 2022-09-23 11:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myblog', '0019_author'),
    ]

    operations = [
        migrations.AddField(
            model_name='bloginfo',
            name='author',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='myblog.author'),
        ),
    ]
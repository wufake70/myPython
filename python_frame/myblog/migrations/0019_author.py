# Generated by Django 3.2.15 on 2022-09-23 11:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myblog', '0018_bloginfo_blogviews'),
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
                ('pwd', models.CharField(max_length=50)),
            ],
        ),
    ]

# Generated by Django 4.2.1 on 2023-06-18 15:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_alter_profile_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='nickname',
            field=models.CharField(max_length=20, unique=True, verbose_name='昵称'),
        ),
    ]

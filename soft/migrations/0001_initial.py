# Generated by Django 4.2.1 on 2023-06-18 14:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SoftMetas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=20, verbose_name='软件分类名称')),
            ],
            options={
                'verbose_name': '软件分类',
                'verbose_name_plural': '软件分类',
            },
        ),
    ]

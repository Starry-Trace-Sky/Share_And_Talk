# Generated by Django 4.2.1 on 2023-06-18 18:17

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0006_alter_articles_likes'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=200, verbose_name='内容')),
                ('pub_date', models.DateTimeField(auto_now_add=True, verbose_name='发布日期')),
                ('modify_date', models.DateTimeField(default=django.utils.timezone.now, editable=False, verbose_name='修改日期')),
                ('article', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.articles', verbose_name='隶属文章')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='作者')),
            ],
            options={
                'verbose_name': '文章',
                'verbose_name_plural': '文章',
            },
        ),
    ]

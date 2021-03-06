# Generated by Django 3.0.3 on 2020-09-24 14:53

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import mdeditor.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, unique=True, verbose_name='分类名')),
                ('slug', models.SlugField(blank=True, default='no-slug', max_length=60)),
            ],
            options={
                'verbose_name': '分类',
                'verbose_name_plural': '分类',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, unique=True, verbose_name='标签名')),
                ('slug', models.SlugField(blank=True, default='no-slug', max_length=60)),
            ],
            options={
                'verbose_name': '标签',
                'verbose_name_plural': '标签',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, unique=True, verbose_name='标题')),
                ('body', mdeditor.fields.MDTextField()),
                ('create_time', models.DateTimeField(default=django.utils.timezone.now, verbose_name='创建时间')),
                ('update_time', models.DateTimeField(default=django.utils.timezone.now, verbose_name='更新时间')),
                ('views', models.IntegerField(default=0, verbose_name='浏览量')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='作者')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='articles.Category', verbose_name='分类')),
                ('tags', models.ManyToManyField(blank=True, to='articles.Tag', verbose_name='标签')),
            ],
            options={
                'verbose_name': '文章',
                'verbose_name_plural': '文章',
            },
        ),
    ]

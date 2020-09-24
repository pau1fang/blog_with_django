from django.db import models
from mdeditor.fields import MDTextField
from django.utils.timezone import now
from django.urls import reverse
from django.conf import settings
# from taggit.managers import TaggableManager


class Article(models.Model):
    """博客文章"""
    title = models.CharField('标题', max_length=200, unique=True)
    body = MDTextField()
    create_time = models.DateTimeField('创建时间', default=now)
    update_time = models.DateTimeField('更新时间', default=now)
    views = models.IntegerField('浏览量', default=0)

    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        verbose_name='作者',
        blank=False,
        null=False
    )
    category = models.ForeignKey(
        'Category',
        on_delete=models.CASCADE,
        verbose_name='分类',
        blank=False,
        null=False
    )
    tags = models.ManyToManyField(
        'Tag',
        verbose_name='标签',
        blank=True,
    )

    class Meta:
        verbose_name = '文章'
        verbose_name_plural = verbose_name

    def next_article(self):
        return Article.objects.filter(id__gt=self.id).order_by('id').first()

    def prev_article(self):
        return Article.objects.filter(id__lt=self.id).first()

    def viewed(self):
        self.views += 1
        self.save(update_fields=['views'])

    def get_absolute_url(self):
        return reverse('articles:article_detail', args=[self.id])


class Category(models.Model):
    """博客分类"""
    name = models.CharField('分类名', max_length=20, unique=True)
    slug = models.SlugField(default='no-slug', max_length=60, blank=True)

    class Meta:
        ordering = ['name']
        verbose_name = '分类'
        verbose_name_plural = verbose_name

    def get_absolute_url(self):
        return reverse('articles:category_detail', kwargs={'category_name': self.slug})

    def __str__(self):
        return self.name


class Tag(models.Model):
    """博客标签"""
    name = models.CharField('标签名', max_length=20, unique=True)
    slug = models.SlugField(default='no-slug', max_length=60, blank=True)

    class Meta:
        ordering = ['name']
        verbose_name = "标签"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('articles:category_detail', kwargs={'category_name': self.slug})



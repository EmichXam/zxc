from django.db import models
from django.db.models import ImageField
from django.urls import reverse

class Article(models.Model):
    article_title = models.CharField('Название урока', max_length=200)
    article_img1 = models.ImageField(upload_to="image/", null=True, blank=True)
    article_img2 = models.ImageField(upload_to="image/", null=True, blank=True)
    article_text = models.TextField('Текст статьи')
    pub_date = models.DateTimeField('Дата публикации')
    slug = models.SlugField(null=False, unique=True)

    def __str__(self):
        return self.article_title

    def get_absolute_url(self):
        return reverse("main:detail", kwargs={"slug": self.slug})

    def get_test_url(self):
        return reverse("main:test_detail", kwargs={"slug": self.slug})

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'



class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    author_name = models.CharField('Никнейм', max_length=200)
    text = models.TextField('Текст комментария')


class Test(models.Model):
    question = models.CharField('Вопрос', max_length=200)
    answer1 = models.CharField('Вариант1', max_length=200)
    answer2 = models.CharField('Вариант2', max_length=200)
    answer3 = models.CharField('Вариант3', max_length=200)
    answer4 = models.CharField('Вариант4', max_length=200)
    correct = models.CharField('Правильный вариант ответа', max_length=200)
    slug = models.SlugField(null=False, unique=False)

    def get_test_url(self):
        return reverse("main:test_detail", kwargs={"slug": self.slug})

    class Meta:
        verbose_name = 'Тест'
        verbose_name_plural = 'Тесты'


class Choice(models.Model):
    question = models.ForeignKey(Test, on_delete=models.CASCADE)
    user = models.CharField(max_length=150, null=False)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

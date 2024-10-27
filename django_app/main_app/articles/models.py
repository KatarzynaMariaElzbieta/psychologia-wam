from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class Tags(models.Model):
    name = models.CharField(verbose_name='tag', max_length=50)

    def __str__(self):
        return self.name


class Article(models.Model):
    create_date = models.DateTimeField(verbose_name="Data_utworzenia", auto_now_add=True)
    update_date = models.DateTimeField(verbose_name="Data_aktualizacji", auto_now=True)
    title = models.CharField(verbose_name="tytuł", max_length=250)
    body = models.TextField(verbose_name="artykuł")
    user_author = models.ForeignKey(User, verbose_name="autor", related_name="author", on_delete=models.CASCADE)
    tags_article = models.ManyToManyField(Tags, verbose_name="tagi")

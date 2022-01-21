from django.db import models


class Phone(models.Model):
    name = models.TextField(verbose_name='название')
    price = models.IntegerField(verbose_name='цена')
    image = models.TextField(verbose_name='картинка')
    release_date = models.DateField(verbose_name='дата релиза')
    lte_exists = models.BooleanField()
    slug = models.SlugField(max_length=250)
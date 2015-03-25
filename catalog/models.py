# -*- coding: utf-8 -*-
from django.db import models


class Category(models.Model):
    title = models.CharField(max_length=250, verbose_name="Название")
    parent = models.ForeignKey("self", verbose_name="Родительская категория", blank=True, null=True, default="-1")
    url = models.CharField("Url", max_length=200, blank=True)
    description = models.CharField("Description", max_length=200, blank=True)
    keywords = models.CharField("Ключевые слова", max_length=200, blank=True)
    step = models.IntegerField("Вложенность", blank=True)
    icon = models.ImageField(verbose_name="Иконка (в меню)", upload_to="static/uploads/", blank=True)
    icon_class = models.CharField("CSS icon (в меню)", max_length=200, blank=True)
    icon_page = models.ImageField(verbose_name="Иконка (на странице)", upload_to="static/uploads/", blank=True)
    icon_class_page = models.CharField("CSS icon (на странице)", max_length=200, blank=True)

    class Meta:
        verbose_name_plural = u"Категории"
        verbose_name = u"Категория"

    def __unicode__(self):
        return self.title


class Video(models.Model):
    title = models.CharField(max_length=250, verbose_name="Название")
    category = models.ForeignKey(Category, verbose_name="Категория", blank=True, null=True, default="-1")
    url = models.CharField("Url", max_length=200, blank=True)
    text = models.TextField("Описание")
    view_count = models.IntegerField("Просмотры", default=0)
    preview = models.ImageField(verbose_name="Превью", upload_to="static/uploads/", blank=True)
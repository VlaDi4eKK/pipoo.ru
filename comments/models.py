# coding=utf-8
from django.db import models
# from account.models import User
from catalog.models import Video
# from forum.models import Forum

class Comment(models.Model):

    # user = models.ForeignKey(User, verbose_name="Пользователь")
    # repost_user = models.ForeignKey(User, verbose_name="Репост от пользовтеля")
    text = models.TextField(verbose_name="Текст комментария")
    video = models.ForeignKey(Video, verbose_name="Видео")
    # forum = models.TextField(Forum, verbose_name="Форум")
    content = models.TextField(verbose_name="Прикрепленные материалы")

    class Meta:
            verbose_name_plural = u"Комментарии"
            verbose_name = u"Коментарий"
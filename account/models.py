# from django.contrib.auth.models import AbstractUser
# from django.utils.translation import ugettext_lazy as _
# from django.db import models
#
# # Модифицируем поле email.
# AbstractUser._meta.get_field('email')._unique = True
# AbstractUser._meta.get_field('email').blank = False
#
#
# class User(AbstractUser):
#     avatar = models.ImageField(_(u'avatar'), upload_to='accounts/avatar/%Y/%m/', blank=True, max_length=1000)
#     birthday = models.DateField(_(u'birthday'), blank=True, null=True)
from django.db import models


class Comment(models.Model):
    hash_object = models.CharField(max_length=200, blank=True)

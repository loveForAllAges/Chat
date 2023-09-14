from django.db import models


class Chat(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)

from django.db import models

from apps.products.models import Category


class Tag(models.Model):
    title = models.CharField(max_length=221)

    def __str__(self):
        return self.title


class Post(models.Model):
    title = models.CharField(max_length=221)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, blank=True, null=True)
    image = models.ImageField(upload_to='blog/', null=True)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    tag = models.ManyToManyField(Tag, blank=True)

    def __str__(self):
        return self.title

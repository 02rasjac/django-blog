from django.db import models

# Create your models here.
class Article(models.Model):
    """Data about blog-posts"""
    title = models.CharField(max_length=100)
    text = models.TextField(max_length=10000)
    published = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

from django.db import models

# Create your models here.


class Article(models.Model):
    author=models.CharField(max_length=100)
    title=models.CharField(max_length=150)
    content=models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)
    is_public=models.BooleanField(default=False)

    def __str__(self):
        return self.title

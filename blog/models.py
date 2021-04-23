from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class article(models.Model):

    title = models.CharField(max_length=255)
    content = models.TextField()
    category = models.CharField(max_length=255)
    slug = models.TextField()
    imgurl = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    # user relation
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return str(self.title)

    class Meta:
        db_table = 'home_article'
        managed = True
        verbose_name = 'Article'
        verbose_name_plural = 'Articles'

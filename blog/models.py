from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class article(models.Model):

    title = models.CharField(max_length=255)
    content = models.TextField()
    category = models.CharField(max_length=255)
    slug = models.TextField()
    imgurl = models.ImageField(
        null=True, blank=True, upload_to='pictures', verbose_name='imgurl')
    created_at = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    # user relation
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return str(self.title)

    def delete(self, *args, **kwargs):
        self.imgurl.delete()
        super().delete(*args, **kwargs)

    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'Article'
        verbose_name_plural = 'Articles'

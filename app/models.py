from django.db import models

class Video(models.Model):
    title = models.CharField(max_length=100)
    file = models.FileField(upload_to='videos/')
    uploaded_at = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='images', verbose_name='画像', null=True, blank=True)
    text = models.TextField('感想', default="", blank=True)
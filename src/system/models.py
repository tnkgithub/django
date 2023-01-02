from django.db import models

# Create your models here.
class ImageCsvModel(models.Model):
    image_name = models.CharField("画像名", max_length=100)
    title = models.CharField("タイトル", max_length=100)

    class Meta:
        verbose_name = 'image'

    def __str__(self):
        return self.title

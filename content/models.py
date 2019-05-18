from django.db import models
from django.utils.safestring import mark_safe


class Album(models.Model):
    title = models.CharField(max_length=200)
    slides = models.TextField()

    def __str__(self):
        return self.title

    def album_slides(self):
        return self.slides.split('\n')


class Photo(models.Model):
    url = models.URLField(max_length=200, unique=True)
    isFeatured = models.BooleanField(default=False)
    updated = models.DateTimeField(auto_now=True)

    def preview(self):
        return mark_safe('<img src="%s" class="image-preview" />' % self.url)

    def __str__(self):
        return self.url

    class Meta:
        ordering=['-updated']


class Video(models.Model):
    url = models.URLField(max_length=200, unique=True)
    isFeatured = models.BooleanField(default=False)
    updated = models.DateTimeField(auto_now=True)
    
    def save(self, *args, **kwargs):
        if self.isFeatured == True:
            Video.objects.filter(isFeatured=True).update(isFeatured=False)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.url

    class Meta:
        ordering=['-updated']

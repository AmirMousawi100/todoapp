from django.db import models
from django.template.defaultfilters import slugify

# Create your models here.


class Books(models.Model):
    title = models.CharField(max_length=100)
    slug = models.CharField(null=True, max_length=100)
    genre = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    isbn = models.CharField(max_length=100)
    count = models.IntegerField(null=True, default=0)
    test = models.CharField(max_length=1, default="l")

    def save(self):
        if not self.slug:
            self.slug = slugify(self.title)
        return super().save()

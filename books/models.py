from django.db import models
from django.db import models
from django.utils import timezone

# Create your models here.


class Book(models.Model):
    title = models.CharField(max_length=200)
    authors = models.CharField(max_length=100)
    publication_date = models.DateField(default=timezone.now)
    publisher = models.CharField(max_length=50)
    summary = models.TextField()
    price = models.FloatField()
    purchase_link = models.URLField()
    cover_img = models.URLField()

    class Meta:
        ordering = ('title',)

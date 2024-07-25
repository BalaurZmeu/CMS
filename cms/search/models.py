from django.db import models
from django.contrib.flatpages.models import FlatPage


class SearchKeyword(models.Model):
    keyword = models.CharField(max_length=50)
    flatpages = models.ForeignKey(FlatPage, on_delete=models.CASCADE, blank=True)

    def __str__(self):
        return self.keyword


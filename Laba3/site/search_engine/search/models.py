from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Indexer(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

    class Meta:
        app_label = 'search'

class Count_in_file(models.Model):
    indexer = models.ForeignKey(Indexer, on_delete=models.CASCADE)
    link = models.CharField(max_length=300, default='')
    countWords = models.IntegerField()

    class Meta:
        app_label = 'search'

    def __str__(self):
        return self.link
    
    def __repr__(self):
        return str((self.link, self.countWords))

class URL(models.Model):
    link = models.CharField(max_length=300)
    description = models.TextField()

    def __str__(self):
        return self.link



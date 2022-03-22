from django.db import models

# Create your models here.

class Note(models.Model):
    title = models.CharField(max_length=200)

    content = models.TextField()

    def __str__(self):
        return '%s %s' % (self.id, self.title)
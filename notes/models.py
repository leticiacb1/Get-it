from django.db import models

# Create your models here.

class Tag(models.Model):
    # Nome da Tag
    tag_name = models.CharField(max_length=200, default='')

    def __str__(self) -> str:
        return '%s' % (self.tag_name)

class Note(models.Model):
    
    title = models.CharField(max_length=200)
    content = models.TextField(default='')
    tag = models.ForeignKey(to=Tag, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return '%s %s' % (self.id, self.title)
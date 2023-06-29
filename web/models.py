from django.db import models

# Create your models here.
class suggest(models.Model):
    word = models.CharField(max_length=250)
    meaning = models.CharField(max_length=250)
    def __str__(self):
        return self.word

class Feedback(models.Model):
    Name = models.CharField(max_length=100)
    Email = models.EmailField()
    Subject = models.CharField(max_length=250)
    Message = models.TextField()
    def __str__(self):
        return self.Name

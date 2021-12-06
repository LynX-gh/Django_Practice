import datetime
from django.utils import timezone

from django.db import models

# Create your models here.
class Question(models.Model):
    # Column Fields
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    # Methods
    def __str__(self):
        return self.question_text
    
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

class Choice(models.Model):
    # Column Fields
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    # Methods
    def __str__(self):
        return self.choice_text

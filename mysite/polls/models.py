from django.db import models


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date published")

    def __str__(self):
        return str(self.id) + '. ' + self.question_text


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return str(self.id) + '. ' + self.choice_text
    
class Cat(models.Model):
    text = models.TextField()

    def __str__(self):
        return self.text
    
class Price(models.Model):
    time=models.CharField(max_length=50)
    close=models.FloatField()
    
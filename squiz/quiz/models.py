from django.db import models
from Users.models import Profile


class Test(models.Model):
    quiz_title = models.CharField(max_length=100)
#    timer = models.TimeField(widget=forms.TimeInput(format='%H:%M'))
    student = models.ManyToManyField(Profile, related_name='student')
    teacher = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='teacher')

    def __str__(self):
        return self.quiz_title


class Question(models.Model):
    quiz = models.ForeignKey(Test, on_delete=models.CASCADE)
    question_text = models.CharField(max_length=1000)

    def __str__(self):
        return self.question_text


class Options(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    option_text = models.CharField(max_length=100)
    is_correct = models.BooleanField(default=False)

    def __str__(self):
        return self.option_text


class Score(models.Model):
    quiz = models.OneToOneField(Test, on_delete=models.CASCADE)
    score = models.IntegerField(default=0)

    def __str__(self):
        return str(self.score)


class Response(models.Model):
    question = models.OneToOneField(Question, on_delete=models.CASCADE)
    selected_option = models.CharField(max_length=2000, null=True, blank=True)

    def __str__(self):
        return self.selected_option


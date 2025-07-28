from django.db import models
from django.conf import settings

class Submission(models.Model):
    student = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    exam = models.ForeignKey('exam.Exam', on_delete=models.CASCADE)
    submitted_at = models.DateTimeField(auto_now_add=True)
    terminated = models.BooleanField(default=False)
    score = models.FloatField(default=0)
    completed = models.BooleanField(default=False)

    class Meta:
        unique_together = ('student', 'exam')  # one submission per exam per user

    def __str__(self):
        return f"{self.student.email} - {self.exam.title}"

    def calculate_score(self):
        correct = sum(1 for answer in self.answers.all() if answer.is_correct())
        self.score = correct
        self.save()
        return self.score


class Answer(models.Model):
    submission = models.ForeignKey(Submission, on_delete=models.CASCADE, related_name='answers')
    question = models.ForeignKey('exam.Question', on_delete=models.CASCADE)
    selected_option = models.ForeignKey('exam.Option', null=True, blank=True, on_delete=models.SET_NULL)

    def __str__(self):
        return f"Answer to: {self.question.text}"

    def is_correct(self):
        return self.selected_option == self.question.correct_option

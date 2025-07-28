from django.db import models
from django.utils.text import slugify

class Exam(models.Model):
    STATE_CHOICES = [
        ('scheduled', 'Scheduled'),
        ('ongoing', 'Ongoing'),
        ('completed', 'Completed'),
        ('cancelled', 'Cancelled'),
    ]
    
    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True, blank=False)
    schedule = models.DateTimeField()
    duration = models.PositiveIntegerField(help_text="Duration in minutes")
    state = models.CharField(max_length=20, choices=STATE_CHOICES, default='scheduled')

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

class Question(models.Model):
    exam = models.ForeignKey(Exam, on_delete=models.CASCADE, related_name='questions')
    text = models.CharField(max_length=500)
    class Meta:
        ordering = ['id'] 
    def __str__(self):
        return self.text

class Option(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='options')
    text = models.CharField(max_length=255)
    is_correct = models.BooleanField(default=False) 

    def __str__(self):
        return self.text
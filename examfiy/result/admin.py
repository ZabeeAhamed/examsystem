from django.contrib import admin
from .models import Submission, Answer

class AnswerInline(admin.TabularInline):
    model = Answer
    extra = 0

@admin.register(Submission)
class SubmissionAdmin(admin.ModelAdmin):
    list_display = ('student', 'exam', 'submitted_at', 'score')
    inlines = [AnswerInline]

admin.site.register(Answer)
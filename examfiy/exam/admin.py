from django.contrib import admin
from .models import Exam, Question, Option
from django import forms
from django.forms.models import BaseInlineFormSet

class OptionInlineFormset(BaseInlineFormSet):
    def clean(self):
        super().clean()
        correct_count = 0
        for form in self.forms:
            if not form.cleaned_data.get('DELETE', False):
                if form.cleaned_data.get('is_correct', False):
                    correct_count += 1
        if correct_count != 1:
            raise forms.ValidationError("There must be exactly one correct option for each question.")
        
class OptionInline(admin.TabularInline):
    model = Option
    extra = 4
    fields = ('text', 'is_correct')  # ✅ show the correct checkbox
    formset = OptionInlineFormset

class QuestionAdmin(admin.ModelAdmin):
    inlines = [OptionInline]
    list_display = ['text', 'exam']
    list_filter = ['exam']
    search_fields = ['text', 'exam__title']
    

class QuestionInline(admin.StackedInline):
    model = Question
    extra = 1

class ExamAdmin(admin.ModelAdmin):
    inlines = [QuestionInline]
    list_display = ['title', 'schedule', 'duration', 'state']
    list_filter = ['state']

admin.site.register(Exam, ExamAdmin)
admin.site.register(Question, QuestionAdmin)
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Exam
from django.shortcuts import render, get_object_or_404, redirect
from .models import Exam, Question, Option
from result.models import Submission, Answer
from django.contrib import messages

@login_required
def exam_list(request):
    exams = Exam.objects.all()
    return render(request, 'exam/exam_list.html', {'exams': exams})



@login_required
def take_exam_combined(request, slug):
    exam = get_object_or_404(Exam, slug=slug)
    questions = exam.questions.all()
    submission, created = Submission.objects.get_or_create(student=request.user, exam=exam)

    if submission.completed:
        messages.info(request, "You have already completed this exam.")
        return redirect('view_result', slug=slug)

    # POST → Save all answers & evaluate
    if request.method == 'POST':
        for question in questions:
            qid = str(question.id)
            selected_option_id = request.POST.get(f'option_{qid}', None)
            if selected_option_id and selected_option_id != 'None':
                option = Option.objects.get(id=selected_option_id)
                Answer.objects.update_or_create(
                  submission=submission,
                  question=question,
                  defaults={'selected_option': option}
                )
            else:
             # Optionally: handle unanswered questions explicitly by clearing the answer or skipping
                Answer.objects.update_or_create(
                submission=submission,
                question=question,
                defaults={'selected_option': None}
                )


        # Evaluate
        answers = Answer.objects.filter(submission=submission)
        correct_count = sum(1 for a in answers if a.selected_option and a.selected_option.is_correct)
        submission.score = correct_count
        submission.completed = True
        submission.save()

        response = redirect('view_result', slug=exam.slug)
        response.set_cookie('clear_exam_data', slug)
        return response

    # Preselected answers (for disabled selection)
    selected_answers = {
        answer.question.id: answer.selected_option_id
        for answer in Answer.objects.filter(submission=submission)
    }

    return render(request, 'exam/take_exam_combined.html', {
        'exam': exam,
        'questions': questions,
        'selected_answers': selected_answers,
        'duration': exam.duration or 30
    })

@login_required
def start_exam_view(request, slug):
    exam = get_object_or_404(Exam, slug=slug)
    return render(request, 'exam/exam_instruction.html', { 'exam': exam })

@login_required
def view_result(request, slug):
    exam = get_object_or_404(Exam, slug=slug)
    submission = Submission.objects.filter(student=request.user, exam=exam).first()

    if not submission:
        messages.error(request, "You haven't taken this exam yet.")
        return redirect('exam_list')

    total_questions = exam.questions.count()
    answers = Answer.objects.filter(submission=submission).select_related('question', 'selected_option')

    return render(request, 'exam/view_result.html', {
        'exam': exam,
        'submission': submission,
        'answers': answers,
        'total_questions': total_questions
    })

@login_required
def my_exam_history(request):
    submissions = Submission.objects.filter(student=request.user).select_related('exam').order_by('-submitted_at')
    return render(request, 'exam/my_exam_history.html', {'submissions': submissions})


from django.urls import path
from exam import views

urlpatterns = [
    path('exam/', views.exam_list, name='exam_list'),
   path('exam/<slug:slug>/instructions/', views.start_exam_view, name='exam_instruction'),
    path('exam/<slug:slug>/start/', views.take_exam_combined, name='take_exam_combined'),
    path('exam/<slug:slug>/result/', views.view_result, name='view_result'),
    path('history/', views.my_exam_history, name='my_exam_history'),

]

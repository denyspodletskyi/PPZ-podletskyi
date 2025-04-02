from django.shortcuts import render
from .models import Question

def question_list(request):
    questions = Question.objects.all()  # Отримуємо всі питання з моделі
    return render(request, 'question_list.html', {'questions': questions})

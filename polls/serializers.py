from rest_framework import serializers
from .models import Question  # імпортуйте вашу модель

class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question  # вказуємо модель, яку серіалізуємо
        fields = '__all__'  # або вказуємо конкретні поля, наприклад: ['id', 'question_text']

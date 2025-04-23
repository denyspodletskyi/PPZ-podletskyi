from django.contrib import admin
from polls import views
from polls.views import QuestionListView
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('polls/', include('polls.urls')),
    path('login/', include('polls.urls')),
    path('', views.question_list, name='question_list'),
    path('api/questions/', QuestionListView.as_view(), name='questions-api'),
    path('polls/', include('polls.urls')),

]

"""squiz URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from quiz import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('Users.urls')),
    path('<username>/quiz/<int:pk>', views.show_quiz, name='show_quiz'),
    path('result/<int:pk>', views.view_result, name='result_quiz'),
    path('<username>/response/<int:pk>', views.view_response, name='response'),
    path('<username>/add_quiz/', views.add_quiz, name="add_quiz"),
    path('<username>/add_quiz/<int:pk>/', views.add_question, name="add_question"),
    path('quiz/<int:pk>/<int:question_no>/', views.quiz_home, name="quiz"),
    path('quiz/score/<int:pk>/', views.evaluate, name="evaluate"),
]

from django.shortcuts import render, redirect
from .models import Profile
from quiz.models import Test, Question, Options, Score
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


def home(request):
    if request.user.is_authenticated:
        all_quiz = Test.objects.all()
        if request.user.profile.role == "Teacher":
            quiz_by_teacher = Test.objects.filter(teacher=request.user.profile)
            return render(request, 'Users/home.html', {'all_quiz': all_quiz, 'quiz_by_teacher': quiz_by_teacher})
        else:
            return render(request, 'Users/home.html', {'all_quiz': all_quiz})
    return render(request, 'Users/home.html', {})


def signin(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = User.objects.filter(username=username)
        error_signin = False
        error_pass = False
        if user:
            user = authenticate(username=username, password=password)
            if user is None:
                error_pass = True
            else:
                login(request, user)
                if user.profile.role == 'Teacher':
                    return redirect('/')
                else:
                    return redirect('/')
        else:
            error_signin = True
        return render(request, template_name='Users/login.html', context={'error_signin': error_signin, 'error_pass': error_pass})

    else:
        return render(request, 'Users/login.html', {})


def register(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        department = request.POST.get('department')
        role = request.POST.get('role')

        user = User.objects.filter(username=username)
        if password != confirm_password:
            error_cnfrmpass = True
            return render(request, 'Users/login.html', {'error_cnfrmpass': error_cnfrmpass})
        if user:
            error_register = True
            return render(request, 'Users/login.html', {'error_register': error_register})
        else:
            User.objects.create_user(username=username, password=password, first_name=first_name, last_name=last_name)
            user = authenticate(username=username, password=password)
            user_profile = Profile.objects.create(user=user, role=role, department=department)
            user.save()
            user_profile.save()
            login(request, user)
            return redirect('/')


def logout_view(request):
    logout(request)
    return redirect('/')


@login_required
def profile(request):
    all_score = Score.objects.filter(student=request.user.profile)
    return render(request, 'Users/profile.html', {'all_score': all_score})


def leaderboard(request, pk):

    all_quiz = Test.objects.all()
    try:
        quiz = Test.objects.get(pk=pk)
    except Test.DoesNotExist:
        return render(request, 'Users/leaderboard.html', {'all_quiz': all_quiz})
    else:
        scores = Score.objects.filter(quiz=quiz)
        dict = {}
        for sc in scores:
            for student_user in sc.student.all():
                dict[student_user] = sc

        return render(request, 'Users/leaderboard.html', {'dict': dict, 'all_quiz': all_quiz, 'current_quiz': quiz})


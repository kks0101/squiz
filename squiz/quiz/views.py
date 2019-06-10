from django.shortcuts import render, redirect
from .models import Test, Question, Options, Score, Response
from Users.models import Profile
from django.contrib.auth.models import User


def quiz_home(request, pk, question_no):
    quiz = Test.objects.get(pk=pk)
    question = Question.objects.get(quiz=quiz, pk=question_no)
    # to get the primary key value of next record(question)
    next_pk = question_no
    for q in Question.objects.filter(quiz=quiz).order_by('-pk'):
        if q.pk > question_no:
            next_pk = q.pk
    quiz.student.add(request.user.profile)
    if request.method == "POST":
        selected_option = request.POST.get('option')
        Response.objects.create(question=question, selected_option=selected_option)
        if question_no < quiz.question_set.last().pk:
            # print('/quiz/' + str(pk) + '/' + str(question_no + 1))
            return redirect('/quiz/' + str(pk) + '/' + str(next_pk))
        else:
            return redirect('/quiz/score/' + str(pk) + '/')
    else:
        return render(request, 'quiz/quiz.html', {'question': question})


def evaluate(request, pk):
    quiz = Test.objects.get(pk=pk)
    questions = Question.objects.filter(quiz=quiz)
    sc = 0
    for question in questions:
        user_response = Response.objects.get(question=question)
        user_answer = str(user_response.selected_option)
        correct_answer = str(Options.objects.get(question=question, is_correct=True))
        # print("cr- " + str(correct_answer) + "  user- "+ str(user_answer))
        # print("Score- " + str(sc))
        if user_answer == correct_answer:
            sc = sc + 1

    Score.objects.create(quiz=quiz, score=sc)

    return render(request, 'quiz/quiz_finish.html', {'score': sc})


def add_quiz(request, username):
    user = User.objects.get(username=username)
    prfl = Profile.objects.get(user=user)
    if not prfl.role == "Teacher":
        error_addquiz = True
        return render(request, 'quiz/add_quiz.html', {'error_addquiz': error_addquiz})
    else:
        error_addquiz = False
        if request.method == "POST":
            quiz_title = request.POST.get('quiz_title')
            t = Test.objects.create(quiz_title=quiz_title, teacher=prfl)
            return redirect('/' + str(username) + '/add_quiz/' + str(t.pk) + '/')

        else:
            return render(request, 'quiz/add_quiz.html', {'error_addquiz': error_addquiz})


def add_question(request, username, pk):
    user = User.objects.get(username=username)
    prfl = Profile.objects.get(user=user)

    if not prfl.role == "Teacher":
        error_addques = True
        return render(request, 'quiz/add_question.html', {'error_addques': error_addques})
    else:
        error_addques = False
        quiz = Test.objects.get(pk=pk, teacher=prfl)
        question = Question.objects.filter(quiz=quiz)
        if request.method == "POST":
            question_text = request.POST.get('question_text')
            option1 = request.POST.get('option1')
            option2 = request.POST.get('option2')
            option3 = request.POST.get('option3')
            option4 = request.POST.get('option4')
            correct_ans = request.POST.get('correct_ans')
            ques = Question.objects.create(quiz=quiz, question_text=question_text)
            Options.objects.create(question=ques, option_text=option1)
            Options.objects.create(question=ques, option_text=option2)
            Options.objects.create(question=ques, option_text=option3)
            Options.objects.create(question=ques, option_text=option4)
            ca = Options.objects.get(question=ques, option_text=correct_ans)
            ca.is_correct = True
            ca.save()
            return redirect('/' + str(username) + '/add_quiz/' + str(pk) + '/')

        else:
            return render(request, 'quiz/add_question.html', {'error_addques': error_addques, 'questions': question, 'quiz': quiz})


def show_quiz(request, username, pk):
    user = User.objects.get(username=username)
    prfl = Profile.objects.get(user=user)

    if not prfl.role == "Teacher":
        error_showques = True
        return render(request, 'quiz/show_question.html', {'error_showques': error_showques})
    else:
        error_showques = False
        all_quiz_by_teacher = Test.objects.filter(teacher=prfl)
        quiz = Test.objects.get(pk=pk, teacher=prfl)
        question = Question.objects.filter(quiz=quiz)
        return render(request, 'quiz/show_question.html', {'error_showques': error_showques, 'questions': question, 'all_quiz': all_quiz_by_teacher})


def view_response(request, username, pk):
    user = User.objects.get(username=username)
    prfl = Profile.objects.get(user=user)

    if not prfl.role == "Student":
        error_viewresponse = True
        return render(request, 'quiz/show_response.html', {'error_viewresponse': error_viewresponse})
    else:
        error_viewresponse = False
        quiz = Test.objects.get(pk=pk, student=prfl)
        question = Question.objects.filter(quiz=quiz)
        return render(request, 'quiz/show_response.html',
                      {'error_viewresponse': error_viewresponse, 'questions': question})


def view_result(request, pk):
    quiz = Test.objects.get(pk=pk)
    all_students = quiz.student.all()
    dict = {}
    for t in all_students:
        q = Test.objects.get(pk=pk, student=t)
        dict[t] = q.score

    return render(request, 'quiz/view_result.html', {'dict': dict, 'current_quiz': quiz})

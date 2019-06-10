from django.shortcuts import render, redirect
from .models import Test, Question, Options, Score, Response
from Users.models import Profile


def quiz_home(request, pk, question_no):
    quiz = Test.objects.get(pk=pk)
    question = Question.objects.get(quiz=quiz, pk=question_no)
    quiz.student.add(request.user.profile)
    if request.method == "POST":
        selected_option = request.POST.get('option')
        Response.objects.create(question=question, selected_option=selected_option)
        if question_no < quiz.question_set.count():
            # print('/quiz/' + str(pk) + '/' + str(question_no + 1))
            return redirect('/quiz/' + str(pk) + '/' + str(question_no+1))
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


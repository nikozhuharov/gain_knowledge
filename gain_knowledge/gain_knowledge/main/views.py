from django import forms
from django.shortcuts import render, redirect

from django.views.generic import ListView, DetailView

# Create your views here.
from gain_knowledge.main.models import Category, Profile, Course, Test, Question, CurrentResult


def show_home(request):
    return render(request, 'home_page.html')


class CategoryListView(ListView):
    model = Category
    template_name = 'list_categories.html'


def list_courses(request, pk):
    context = {
        'courses': Course.objects.filter(category=Category.objects.get(pk=pk))
    }
    return render(request, 'list_courses.html', context)


class CourseDetailView(DetailView):
    model = Course
    template_name = 'course_details.html'
    context_object_name = 'course_detail'


def list_tests(request, pk):
    context = {
        'tests': Test.objects.filter(course_id=pk)
    }
    return render(request, 'list_tests.html', context)


def display_question(request, pk):
    question = Question.objects.get(pk=pk)


    options = [("A", question.first_option),
               ("B", question.second_option),
               ("C", question.third_option),
               ("D", question.fourth_option),
               ]

    FIRST_OPTION = question.first_option
    SECOND_OPTION = question.second_option
    THIRD_OPTION = question.third_option
    FOURTH_OPTION = question.fourth_option

    OPTIONS = [(x, x) for x in (FIRST_OPTION, SECOND_OPTION, THIRD_OPTION, FOURTH_OPTION)]

    class QuestionForm(forms.Form):
        answer = forms.CharField(label=question.title, widget=forms.RadioSelect(choices=options))

    if request.method == 'POST':
        form = QuestionForm(request.POST)
        current_result = CurrentResult.objects.get(pk=1)
        if form.is_valid():
            if form.cleaned_data['answer'] == question.correct_answer:
                current_result.correct_answers += 1
            else:
                current_result.incorrect_answers += 1
            current_result.save()

            if pk < len([x for x in Question.objects.all()]):
                return redirect('display question', pk=pk+1)
            else:
                return redirect('final score')
    else:
        form = QuestionForm()

    context = {
        'form': form,
        'question': question
    }

    return render(request, 'display_question.html', context)


def final_score(request):
    current_result = CurrentResult.objects.get(pk=1)
    total_answers = current_result.correct_answers + current_result.incorrect_answers
    correct_answers = current_result.correct_answers
    percentage = int(correct_answers/total_answers*100)
    context = {
        'correct_answers': correct_answers,
        'total_answers': total_answers,
        'percentage': percentage
    }
    current_result.correct_answers = 0
    current_result.incorrect_answers = 0
    current_result.save()

    return render(request, 'final_score.html', context)


def show_profile(request):
    pass


def create_profile(request):
    pass


def edit_profile(request):
    pass


def delete_profile(request):
    pass

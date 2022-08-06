from django.shortcuts import render, get_object_or_404
from .models import Article, Test, Choice
from django.views.generic import DetailView
from django.http import HttpResponseRedirect
from django.urls import reverse

def index(request):

    return render(request, 'main/index.html')

def about(request):
    return render(request, 'main/about.html')

def section(request):
    article = Article.objects.order_by('-id')
    return render(request, 'main/section.html', {'title':'Теория', 'article': article})

def tests(request):
    article = Article.objects.order_by('-id')
    return render(request, 'main/tests.html', {'title':'Теория', 'article': article})
#https://docs.djangoproject.com/en/4.0/ref/class-based-views/generic-display/#detailview



class test_detail(DetailView):
    model = Test



    def detail_view(request, slug):
        a = Test.objects.all()
        context = {'a': a}
        return render(request, 'main/test_detail.html', context)

def leave_comment(request, slug):
    a = Article.objects.get(slug=slug)

    a.comment_set.create(author_name=request.POST['name'], text=request.POST['text'])

    return HttpResponseRedirect(reverse('main:detail', args=(slug,)))



def test_detail(request, slug):
    tests = Test.objects.filter( slug=slug)
    context = {'tests':tests, 'slug':slug}
    return render(request, 'main/test_detail.html', context)



def article_detail(request, slug):
    model = Article.objects.get( slug = slug)
    comments = model.comment_set.all()
    context = {'object': model, 'comments':comments}
    return render(request, 'main/article_detail.html', context)

def result(request, slug):
    tests = Test.objects.filter( slug=slug)

    context = {'tests':tests,'slug':slug}
    return render(request, 'main/result.html', context)

def leave_test(request, slug):
    tests = Test.objects.filter( slug=slug) 
    for test in tests:
        answer = request.POST[test.question]
        if answer == test.correct:
            test.choice_set.create(choice_text=test.question,votes='1')
        else:
            test.choice_set.create(choice_text=test.question,votes='0')

    return HttpResponseRedirect(reverse('main:result', args=(slug,)))
from django.contrib.auth.decorators import login_required
from queue import Empty
from django.shortcuts import render
from question.models import Question, Comment
from recipe.models import Recipe
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

from django.db.models import Max

def main_list(request):
    recipe_1 = Recipe.objects.annotate(recipe_likes=Max('like_users')).order_by('-recipe_likes').first()
    recipe_2 = Recipe.objects.annotate(recipe_likes=Max('like_users')).order_by('recipe_likes').exclude(id=recipe_1.id).last()
    recipe_3 = Recipe.objects.annotate(recipe_likes=Max('like_users')).order_by('recipe_likes').exclude(id=recipe_1.id).exclude(id=recipe_2.id).last()
    recipe_4 = Recipe.objects.annotate(recipe_likes=Max('like_users')).order_by('recipe_likes').exclude(id=recipe_1.id).exclude(id=recipe_2.id).exclude(id=recipe_3.id).last()
    recipe_5 = Recipe.objects.annotate(recipe_likes=Max('like_users')).order_by('recipe_likes').exclude(id=recipe_1.id).exclude(id=recipe_2.id).exclude(id=recipe_3.id).exclude(id=recipe_4.id).last()
    recipe_6 = Recipe.objects.annotate(recipe_likes=Max('like_users')).order_by('recipe_likes').exclude(id=recipe_1.id).exclude(id=recipe_2.id).exclude(id=recipe_3.id).exclude(id=recipe_4.id).exclude(id=recipe_5.id).last()
    
    question_1 = Question.objects.last()
    question_2 = Question.objects.filter(id__lt=question_1.id).last()
    question_3 = Question.objects.filter(id__lt=question_2.id).last()
    question_4 = Question.objects.filter(id__lt=question_3.id).last()
    question_5 = Question.objects.filter(id__lt=question_4.id).last()
    question_6 = Question.objects.filter(id__lt=question_5.id).last()
    
    return render(
        request,
        'main/main_list.html',
        {
            'recipe_1': recipe_1,
            'recipe_2': recipe_2,
            'recipe_3': recipe_3,
            'recipe_4': recipe_4,
            'recipe_5': recipe_5,
            'recipe_6': recipe_6,

            'question_1': question_1,
            'question_2': question_2,
            'question_3': question_3,
            'question_4': question_4,
            'question_5': question_5,
            'question_6': question_6,
        }
    )
    
@login_required(login_url='login')
def my_list(request):
    recipe = Recipe.objects.filter(author=request.user).all().order_by('-pk')
    
    page = request.GET.get('page')
    paginator = Paginator(recipe, 10)
    
    try:
        page_obj = paginator.page(page)
    except PageNotAnInteger:
        page = 1
        page_obj = paginator.page(page)
    except EmptyPage:
        page = paginator.num_pages
        page_obj = paginator.page(page)
    
    return render(
        request,
        'main/my_list.html',
        {
            'recipe' : recipe,
            'page_obj' : page_obj,
            'paginator': paginator,
        }
    )

@login_required(login_url='login')
def my_list_question(request):  
    question = Question.objects.filter(author=request.user).all().order_by('-pk')
    
    page = request.GET.get('page')
    paginator = Paginator(question, 10)
    
    try:
        page_obj = paginator.page(page)
    except PageNotAnInteger:
        page = 1
        page_obj = paginator.page(page)
    except EmptyPage:
        page = paginator.num_pages
        page_obj = paginator.page(page)
    
    return render(
        request,
        'main/my_list_question.html',
        {
            'question' : question,
            'page_obj' : page_obj,
            'paginator': paginator,
        }
    )

@login_required(login_url='login')
def my_list_likes(request):
    recipe = Recipe.objects.filter(like_users=request.user).all().order_by('-pk')
    
    page = request.GET.get('page')
    paginator = Paginator(recipe, 10)
    
    try:
        page_obj = paginator.page(page)
    except PageNotAnInteger:
        page = 1
        page_obj = paginator.page(page)
    except EmptyPage:
        page = paginator.num_pages
        page_obj = paginator.page(page)
    
    return render(
        request,
        'main/my_list_likes.html',
        {
            'recipe' : recipe,
            'page_obj' : page_obj,
            'paginator': paginator,
        }
    )

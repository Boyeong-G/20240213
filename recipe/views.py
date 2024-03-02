from django.contrib.auth.decorators import login_required
from django.db.models import Max
from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from .models import Recipe
from .forms import RecipeForm
from django.db.models import Q

def recipe_list(request):
    recipe = Recipe.objects.all().order_by('pk')
    search_keyword = request.GET.get('searchR', '')
    
    if search_keyword :
        search_recipe_list = recipe.filter(Q(dish_name__icontains=search_keyword) | Q (ingredient__icontains=search_keyword) | Q (recipe__icontains=search_keyword))
        return render(
            request,
            'recipe/recipe_list.html',
            {
                'recipe': recipe,
                'searchR': search_keyword,
                'search_recipe_list': search_recipe_list,
            }
        )
    
    return render(
        request,
        'recipe/recipe_list.html',
        {
            'recipe': recipe,
        }
    )

def recipe_list_hot(request):
    recipe = Recipe.objects.all().annotate(recipe_likes=Max('like_users')).order_by('-recipe_likes')
    
    return render(
        request,
        'recipe/recipe_list_hot.html',
        {
            'recipe': recipe,
        }
    )

def recipe_list_recent(request):
    recipe = Recipe.objects.all().order_by('-pk')
    
    return render(
        request,
        'recipe/recipe_list_recent.html',
        {
            'recipe': recipe,
        }
    )

def recipe_detail(request, pk):
    recipe = Recipe.objects.get(pk=pk)
    
    return render(
        request,
        'recipe/recipe_detail.html',
        {
            'recipe': recipe,
        }
    )

@login_required(login_url='login')
def likes(request, pk):
    recipe = Recipe.objects.get(pk=pk)
    
    if request.user.is_authenticated:
        if recipe.like_users.filter(pk=request.user.pk).exists():
            recipe.like_users.remove(request.user)
        else:
            recipe.like_users.add(request.user)
            
    return render(
        request,
        'recipe/recipe_detail.html',
        {
            'recipe': recipe,
        }
    )

@login_required(login_url='login')
@csrf_exempt
def recipe_create(request):
    if request.method == "POST":
        form = RecipeForm(request.POST, request.FILES)
        if form.is_valid():
            recipe = Recipe()
            recipe.dish_name = form.cleaned_data['dish_name']
            recipe.ingredient = form.cleaned_data['ingredient']
            recipe.recipe = form.cleaned_data['recipe']
            recipe.head_image = request.FILES.get('head_image', None)
            recipe.author = request.user
            recipe.save()
            return redirect(recipe)
    else:
        form = RecipeForm()
        
    return render(
        request,
        'recipe/recipe_form.html',
        {
            'form': form
        }
    )

@login_required(login_url='login')
@csrf_exempt
def recipe_edit(request, pk):
    recipe = Recipe.objects.get(id=pk)
    if request.method == "POST":
        form = RecipeForm(request.POST, request.FILES)
        if form.is_valid():
            recipe.dish_name = form.cleaned_data['dish_name']
            recipe.ingredient = form.cleaned_data['ingredient']
            recipe.recipe = form.cleaned_data['recipe']
            recipe.head_image = request.FILES.get('head_image', None)
            recipe.save()
        return redirect(recipe)
    else:
        form = RecipeForm(instance=recipe)
        context = {
            'form': form,
            'writing': True,
            'now': 'edit',
        }
        
    return render(
        request,
        'recipe/recipe_form_edit.html',
        context
    )

def recipe_delete(request, pk):
    question = Recipe.objects.get(id=pk)
    question.delete()
    
    return redirect('../')
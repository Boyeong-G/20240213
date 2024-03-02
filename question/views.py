from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render, redirect, get_object_or_404
from .models import Comment, Question
from .forms import QuestionForm, CommentForm
from django.db.models import Q

def question_list(request):
    question = Question.objects.all().order_by('-pk')
    search_keyword = request.GET.get('searchQ', '')
    
    if search_keyword :
        search_question_list = question.filter(Q (summary__icontains=search_keyword) | Q (question__icontains=search_keyword))
        return render(
            request,
            'question/question_list.html',
            {
                'question': question,
                'searchQ': search_keyword,
                'search_question_list': search_question_list,
            }
        )
    
    return render(
        request,
        'question/question_list.html',
        {
            'question': question,
        }
    )

def question_detail(request, pk):
    question = Question.objects.get(pk=pk)
    comments = Comment.objects.filter(question=question)
    comments_counts = Comment.objects.filter(question=question).count()
    comment_form = CommentForm
    
    return render(
        request,
        'question/question_detail.html',
        {
            'question': question,
            'comments': comments,
            'comments_counts': comments_counts,
            'comment_form': comment_form,
        }
    )

@login_required(login_url='login')
@csrf_exempt
def new_comment(request, pk):
    if request.user.is_authenticated:
        question = get_object_or_404(Question, pk=pk)
        if request.method == 'POST':
            comment_form = CommentForm(request.POST)
            if comment_form.is_valid():
                comment = comment_form.save(commit=False)
                comment.question = question
                comment.author = request.user
                comment.save()
                return redirect(comment.get_absolute_url())
            else:
                return redirect(question.get_absolute_url())
        else:
            raise PermissionDenied
        
def delete_comment(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    question = comment.question
    
    if request.user.is_authenticated and request.user == comment.author:
        comment.delete()
        return redirect(question.get_absolute_url())
    else:
        raise PermissionDenied
    

@login_required(login_url='login')
@csrf_exempt
def question_create(request):
    if request.method == "POST":
        form = QuestionForm(request.POST, request.FILES)
        if form.is_valid():
            question = Question()
            question.summary = form.cleaned_data['summary']
            question.question = form.cleaned_data['question']
            question.head_image = request.FILES.get('head_image', None)
            question.author = request.user
            question.save()
            return redirect(question)
    else:
        form = QuestionForm()
        
    return render(
        request,
        'question/question_form.html',
        {
            'form': form
        }
    )

@login_required(login_url='login')
@csrf_exempt
def question_edit(request, pk):
    question = Question.objects.get(id=pk)
    if request.method == "POST":
        form = QuestionForm(request.POST, request.FILES)
        if form.is_valid():
            question.summary = form.cleaned_data['summary']
            question.question = form.cleaned_data['question']
            question.head_image = request.FILES.get('head_image', None)
            question.save()
        return redirect(question)
    else:
        form = QuestionForm(instance=question)
        context = {
            'form': form,
            'writing': True,
            'now': 'edit',
        }
        
    return render(
        request,
        'question/question_form_edit.html',
        context
    )

def question_delete(request, pk):
    question = Question.objects.get(id=pk)
    question.delete()
    
    return redirect('../')
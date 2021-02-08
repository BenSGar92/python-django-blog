from django.shortcuts import render, redirect
from.models import Article
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from . import forms


# Create your views here.
def article_list(request):
    articles = Article.objects.all().order_by('date') #this will grab all the records from this database - order_by() lets you order them by anything in the Class...like the date
    return render(request, 'articles/article_list.html', { 'articlesArticles': articles })

def article_detail(request, slug):
    # return HttpResponse(slug)
    article = Article.objects.get(slug=slug)
    return render(request, 'articles/article_detail.html', { 'article':article })

#we want to protect this page and make sure people are logged in to access this page -  we will use a decorator and import it in above
# we also want to redirect to correct page after login - such as the create page - within login.html we write an if statement with some syntax that does just that within a hidden input
@login_required(login_url='/accounts/login/')
def article_create(request):
    if request.method == 'POST':
        form = forms.CreateArticle(request.POST, request.FILES)
        if form.is_valid():
            # save article to db = commit=False saves this action and we save that action to a new variable
            instance = form.save(commit=False)
            instance.author = request.user
            instance.save()
            return redirect('articles:list')
    else:
    #creating a new instance of model form
        form = forms.CreateArticle()
    return render(request, 'articles/article_create.html', { 'form': form })
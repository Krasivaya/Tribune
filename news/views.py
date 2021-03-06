from django.http import HttpResponse, Http404, HttpResponseRedirect
import datetime as dt
from django.shortcuts import render, redirect
from .models import Article, NewsletterSubscriber
from .forms import NewsletterForm, ArticleForm
from .email import welcome_mail
from django.contrib.auth.decorators import login_required


# News of Today
def news_of_day(request):
    date = dt.date.today()
    news = Article.todays_news()

    if request.method == 'POST':
        form = NewsletterForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            subscriber = NewsletterSubscriber(name = name, email = email)
            subscriber.save()

            # Send welcome email
            welcome_mail(name, email)
            HttpResponseRedirect('news_of_day')
    else:
        form = NewsletterForm()

    return render(
        request,
        'all-news/today-news.html',
        {
            "date": date,
            "news":news,
            "letterForm": form
        }
    )

# News of Past days
def past_days_news(request, past_dates):
    try:
        date = dt.datetime.strptime(past_dates, '%Y-%m-%d').date()
    except ValueError:
        raise Http404()

    if date == dt.date.today():
        return redirect(news_of_day)
    
    news = Article.archived_news(date)
    return render(
        request,
        'all-news/past-news.html',
        {
            "date": date,
            "news": news
        }
    )

# A single article
@login_required(login_url = '/accounts/login/')
def article(request, article_id):
    try:
        article = Article.objects.get(id = article_id)
    except DoesNotExist:
        raise Http404()
    return render(
        request,
        'all-news/article.html',
        {
            "newsArticle": article
        }
    )

# Create A Post
@login_required(login_url = '/accounts/login/')
def new_article(request):
    current_user = request.user
    if request.method == 'POST':
        form = ArticleForm(request.POST, request.FILES)
        if form.is_valid():
            article = form.save(commit=False)
            article.editor = current_user
            article.save()
        return redirect('news_of_day')
    else:
        form = ArticleForm()

    return render(
        request,
        'all-news/new_article',
        {
            'form': form,
        }
    )

# Search News 
def search_results(request):
    if 'article' in request.GET and request.GET['article']:
        search_term = request.GET.get('article')
        searched_articles = Article.search_by_title(search_term)
        title = f'Searching for {search_term}'
        message = f"{search_term}"

        return render(
            request,
            'all-news/search.html',
            {
                "articles": searched_articles,
                "message": message,
                "title": title
            }
        )
    else:
        message = "You haven't searched for any term"
        return render(request,'all-news/search.html',{"message":message})
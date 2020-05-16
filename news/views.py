from django.http import HttpResponse, Http404, HttpResponseRedirect
import datetime as dt
from django.shortcuts import render, redirect
from .models import Article, NewsletterSubscriber
from .forms import NewsletterForm


# News of Today
def news_of_day(request):
    date = dt.date.today()
    news = Article.todays_news()

    if request.method == 'POST':
        form = NewsletterForm(request.POST)
        if form.is_valid:
            name = form.cleaned_date['name']
            email = form.cleaned_date['email']
            subscriber = NewsletterSubscriber(name = name, email = email)
            subscriber.save()
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
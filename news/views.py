from django.http import HttpResponse, Http404
import datetime as dt
from django.shortcuts import render, redirect
from .models import Article


# News of Today
def news_of_day(request):
    date = dt.date.today()
    news = Article.todays_news()
    return render(
        request,
        'all-news/today-news.html',
        {
            "date": date,
            "news":news
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
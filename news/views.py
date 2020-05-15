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
    return render(
        request,
        'all-news/past-news.html',
        {"date": date}
    )
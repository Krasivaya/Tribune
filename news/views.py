from django.http import HttpResponse, Http404
import datetime as dt
from django.shortcuts import render

# Welcome Page
def welcome(request):
    return render(
        request,
        'welcome.html'
    )

# News of Today
def news_of_day(request):
    date = dt.date.today()
    return render(
        request,
        'all-news/today-news.html',
        {"date": date}
    )

# News of Past days
def past_days_news(request, past_dates):
    try:
        date = dt.datetime.strptime(past_dates, '%Y-%m-%d').date()
    except ValueError:
        raise Http404()

    day = convert_dates(date)
    html = f'''
            <html>
                <body>
                    <h1>
                        News for {day}, {date.day} - {date.month} - {date.year}
                    </h1>
                </body>
            </html>
            '''
    return HttpResponse(
        html
    )
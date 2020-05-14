from django.http import HttpResponse
import datetime as dt

# Welcome Page
def welcome(request):
    return HttpResponse(
        'Welcome to the Tribune'
    )

# News of Today
def news_of_day(request):
    date = dt.date.today()
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

# Convert Dates
def convert_dates(dates):
    day_number = dt.date.weekday(dates)
    days = ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']
    day = days[day_number]
    return day
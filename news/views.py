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
    html = f'''
            <html>
                <body>
                    <h1>
                        {date.day} - {date.month} - {date.year}
                    </h1>
                </body>
            </html>
            '''
    return HttpResponse(
        html
    )
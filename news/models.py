from django.db import models
import datetime as dt

# Editor Model
class Editor(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField()
    phone_number = models.CharField(max_length=30, blank=True)

    def __str__(self):
        return self.first_name

    def save_editor(self):
        return self.save()

#Tag Model
class Tag(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name

    def save_tag(self):
        return self.save()

# Article Model
class Article(models.Model):
    title = models.CharField(max_length=100)
    post = models.TextField()
    editor = models.ForeignKey(Editor)
    tags = models.ManyToManyField(Tag)
    pub_date = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return self.title
    
    def save_article(self):
        return self.save()

    @classmethod
    def todays_news(cls):
        today = dt.date.today()
        news = cls.objects.filter(pub_date__date = today)
        return news

    @classmethod
    def archived_news(cls, days_date):
        news = cls.objects.filter(pub_date__date = days_date)
        return news
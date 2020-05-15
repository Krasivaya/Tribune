from django.test import TestCase
from .models import Editor, Tag, Article
import datetime as dt

# Editor tests
class EditorTestClass(TestCase):
    # Setup Method
    def setUp(self):
        self.carine = Editor(first_name='Carine', last_name='SEMWAGA', email='semwagacarine@gmail.com')

    # Test instance
    def test_instance(self):
        self.assertTrue(isinstance(self.carine, Editor))

    # Test save method
    def test_save_method(self):
        self.carine.save_editor()
        editor = Editor.objects.all()
        self.assertTrue(len(editor) > 0)

    # Test update method
    def test_update_method(self):
        Editor.objects.filter(first_name='Carine').update(first_name='Cary')

    # Test delete method
    def tearDown(self):
        Editor.objects.all().delete()
    
# Tag Tests
class TagTestClass(TestCase):
    # Setup method
    def setUp(self):
        self.new_tag = Tag(name='Testing')

    # Test instance
    def test_instance(self):
        self.assertTrue(isinstance(self.new_tag, Tag))

    # Test save method
    def test_save_method(self):
        self.new_tag.save_tag()
        tag = Tag.objects.all()
        self.assertTrue(len(tag) > 0)

    # Test update method
    def test_update_method(self):
        Tag.objects.filter(name='Testing').update(name='new_testing')

    # Test delete method
    def tearDown(self):
        Tag.objects.all().delete()

# Article Tests 
class ArticleTestClass(TestCase):
    # Setup method
    def setUp(self):
        # Creating an Editor
        self.carine = Editor(first_name='Carine', last_name='SEMWAGA', email='semwagacarine@gmail.com')
        self.carine.save_editor()

        # Creating a Tag
        self.new_tag = Tag(name = 'Testing')
        self.new_tag.save_tag()

        # Creating an Article
        self.new_article = Article(
            title = 'Test Article',
            post = 'This is a random testing article',
            editor = self.carine
        )
        self.new_article.save_article()

        # Many to Many Rel
        self.new_article.tags.add(self.new_tag)
    
    # Test instance
    def test_instance(self):
        self.assertTrue(isinstance(self.new_article, Article))

    # Test save method
    def test_save_method(self):
        self.new_article.save_article()
        article = Article.objects.all()
        self.assertTrue(len(article) > 0)

    # Test today's news method
    def test_todays_news(self):
        today_news = Article.todays_news()
        self.assertTrue(len(today_news) > 0)

    # Test archived news method
    def test_archived_news(self):
        test_date = '2019-08-12'
        date = dt.datetime.strptime(test_date, '%Y-%m-%d').date()
        day_news = Article.archived_news(date)
        self.assertTrue(len(day_news) == 0)

    # Test search article method
    def test_search_by_title(self):
        search_term = 'Test Article'
        search_results = Article.search_by_title(search_term)
        self.assertTrue(len(search_results) > 0)

    # Test delete method
    def tearDown(self):
        Editor.objects.all().delete()
        Tag.objects.all().delete()
        Article.objects.all().delete()

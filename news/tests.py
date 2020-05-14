from django.test import TestCase
from .models import Editor, tags, Article

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
        self.carine.update_editor()

    # Test delete method
    def test_delete_method(self):
        self.carine.delete_editor()
        editor = Editor.objects.all()
        self.assertTrue(len(editor) == 0)
    
# Tags Tests
class tagsTestClass(TestCase):
    # Setup method
    def setUp(self):
        self.sports = tags(name='Sports')

    # Test instance
    def test_instance(self):
        self.assertTrue(isinstance(self.sports, tags))

    # Test save method
    def test_save_method(self):
        self.sports.save_tag()
        tag = tags.objects.all()
        self.assertTrue(len(tag) > 0)

    # Test update method
    def test_update_method(self):
        self.sports.update_tag()
        tag = tags.objects.all()

    # Test delete method
    def test_delete_method(self):
        self.sports.delete_tag()
        tag = tags.objects.all()
        self.assertTrue(len(tag)== 0)

# Test Articles
class ArticleTestClass(TestCase):
    # Setup method
    def setUp(self):
        self.django = Article(
            title = 'Install Django Framework',
            post = 'First create a virtualen with python packages'
        )
    
    # Test instance
    def test_instance(self):
        self.assertTrue(isinstance(self.django, Article))

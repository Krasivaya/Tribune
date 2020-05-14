from django.db import models

# Editor Model
class Editor(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField()

    def __str__(self):
        return self.first_name

    def save_editor(self):
        return self.save()
    
    def update_editor(self):
        return Editor.objects.filter(id=1).update(first_name='Cary')
    
    def delete_editor(self):
        return Editor.objects.filter(id=1).delete()

#Tag Model
class tags(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name

    def save_tag(self):
        return self.save()

    def update_tag(self):
        return tags.objects.filter(id=1).update(name='Music')

    def delete_tag(self):
        return tags.objects.filter(id=1).delete()

# Article Model
class Article(models.Model):
    title = models.CharField(max_length=100)
    post = models.TextField()
    editor = models.ForeignKey(Editor)
    tags = models.ManyToManyField(tags)
    pub_date = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return self.title
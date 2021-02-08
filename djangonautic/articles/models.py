from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField()
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    thumb = models.ImageField(default='default.png', blank=True)
    #begin foreign key tutorial - User imported above
    author = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    # add in author later

    def __str__(self):
        return self.title

    #here we are only showing a snippet of the body on the main article page and then on line 13 of article_list we have added this function
    def snippet(self):
        return self.body[:50] + '...'




#COMMANDS FOR MIGRATING(to a database after setting up a model):
#python manage.py makemigrations
#python manage.py migrate

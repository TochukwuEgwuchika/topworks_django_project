from django.db import models
from django.forms import ModelForm
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User
# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length = 200)
    image = models.ImageField(upload_to = 'images', blank = True, null = True)
    #content = models.TextField()
    content = RichTextField(blank = True, null = True)
    author = models.CharField(max_length = 100, default = 'Topworks')
    published_date = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return self.title

    def get_comment_number(self):
        return Comment.objects.filter(post = self).count()

class Comment(models.Model):
    content = models.TextField(null = False, blank = False)
    commenter = models.ForeignKey(User, on_delete = models.CASCADE, related_name = 'comments')
    post = models.ForeignKey(Post, on_delete = models.CASCADE, related_name = 'comments')
    comment_time = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return "Comment by "+ self.commenter.first_name

    def get_initials(self):
        try:
            initial = str(self.commenter.first_name)[0]
        except:
            initial = str(self.commenter.username)[0]
        

        return initial

class Message(models.Model):
    sender = models.CharField(max_length = 120, null = False)
    email = models.CharField(max_length = 120, null = False)
    subject = models.CharField(max_length = 120, null = False)
    message = models.TextField(null = False)    

class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = '__all__'


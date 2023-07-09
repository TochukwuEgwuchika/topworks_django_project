from . import views
from django.urls import path

urlpatterns = [
    path('view-post/<int:post_id>', views.view_post, name ='view-post'),
    path('blog', views.blog, name='blog'),
    path('post-comment', views.post_comment, name = 'post-comment'),
]
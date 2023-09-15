from django.urls import path
from .views import bloghome,blogpost,postComment
urlpatterns = [
    path('',bloghome,name='Bloghome'),
    path('blogpost/<int:id>',blogpost,name='blogs'),
    # API to post a comment
    path('postComment/',postComment,name='postComment'),
 ]
 
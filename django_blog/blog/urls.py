from django.urls import path,include
from .views import (home,
                    PostList,
                    post_update,
                    about,
                    PostDetailView,
                    PostCreateView,
                    PostUpdateView,
                    PostDeleteView,
                    UserPostList)



urlpatterns = [
    path('',PostList.as_view(), name = 'blog-home'),
    path('user/<str:username>',UserPostList.as_view(), name = 'user-post'),
    path('about/',about, name = 'blog-about'),
    # path('post/<int:pk>',post_update, name = 'blog-post-update'),
    path('post/<int:pk>',PostDetailView.as_view(), name = 'post-detail'),
    path('post/<int:pk>/update',PostUpdateView.as_view(), name = 'post-update'),
    path('post/<int:pk>/delete',PostDeleteView.as_view(), name = 'post-delete'),
    path('post/new',PostCreateView.as_view(), name = 'post-creation'),
]

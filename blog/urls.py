from django.urls import path 
from . import views


urlpatterns = [
    path('author/posts', views.post_list, name='posts-list'),
    path('post-list/', views.PostListView.as_view(), name='post-list'),
    # path('post-list/', views.post_list, name='post-list'),
    path('post-detail/<int:pk>/', views.PostDetailView.as_view(), name='post-detail'),
    # path('post-detail/<int:pk>/', views.post_detail, name='post-detail'),
    path('post/new/', views.PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/update/', views.PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', views.PostDeleteView.as_view(), name='post-delete'),
]

# create alarm clock with python
# https://www.youtube.com/watch?v=X_Q-_X_Q-_X

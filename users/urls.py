from django.urls import path
from . import views


urlpatterns = [
    path('register/', views.register, name='register'),
    # path('login/', views.login, name='login'),
    path('login/', views.UserLoginView.as_view(), name='login'),
    path('logout/', views.logout, name='logout'),
#     path('edit-profile/', views.UserProfileView.as_view(), name='edit-profile'),
    path('edit-profile/', views.edit_profile, name='edit-profile'),
    path('profile/', views.UserProfileView.as_view(), name='profile'),
]
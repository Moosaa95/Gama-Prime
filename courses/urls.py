from django.urls import path
from . import views


urlpatterns = [
    # path('', views.course_index, name='course'),
    path('programming/', views.ProgrammingListView.as_view(), name='programming'),
    path('programming/<slug:slug>/', views.ProgrammingDetailView.as_view(), name='programming-detail'),
    path('programming/<int:pk>/update/', views.ProgrammingUpdateView.as_view(), name='programming-update'),
    path('programming/<int:pk>/delete/', views.ProgrammingDeleteView.as_view(), name='programming-delete'),
    path('take-course/', views.take_course, name='take-course'),
    # path('business/', views.BusinessListView.as_view(), name='business'),
    path('design/', views.DesignListView.as_view(), name='design'),
    path('design/<slug:slug>/', views.DesignDetailView.as_view(), name='design-detail'),
    path('design/<int:pk>/update/', views.DesignUpdateView.as_view(), name='design-update'),
    path('design/<int:pk>/delete/', views.DesignDeleteView.as_view(), name='design-delete'),
    path('management/', views.ManagementListView.as_view(), name='management'),
    path('management/<slug:slug>/', views.ManagementDetailView.as_view(), name='management-detail'),
    path('management/<int:pk>/update/', views.ManagementUpdateView.as_view(), name='management-update'),
    path('management/<int:pk>/delete/', views.ManagementDeleteView.as_view(), name='management-delete'),
    path('business/', views.BusinessListView.as_view(), name='business'),
    path('business/<slug:slug>/', views.BusinessDetailView.as_view(), name='business-detail'),
    path('business/<int:pk>/update/', views.BusinessUpdateView.as_view(), name='business-update'),
    path('business/<int:pk>/delete/', views.BusinessDeleteView.as_view(), name='business-delete'),
    
    # path('management/', views.ManagementListView.as_view(), name='management'),
]
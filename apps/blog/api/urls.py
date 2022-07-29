from django.urls import path
from . import views


urlpatterns = [
    path('tag/list/', views.TagListAPIView.as_view()),
    path('tag/create/', views.TagCreateAPIView.as_view()),
    path('tag/rud/<int:pk>/', views.TagRUDAPIView.as_view()),

    path('post/list/', views.PostListAPIView.as_view()),
    path('post/create/', views.PostCreateAPIView.as_view()),
    path('post/rud/<int:pk>/', views.PostRUDAPIView.as_view()),

]

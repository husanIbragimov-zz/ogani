from django.urls import path, include
from .views import blog_detail, blog_list

app_name = 'blog'

urlpatterns = [
    path('', blog_list, name='blog_list'),
    path('detail/<int:pk>/', blog_detail, name='blog_detail'),

    path('api/', include('apps.blog.api.urls')),

]

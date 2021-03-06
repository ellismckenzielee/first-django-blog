from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/new/', views.post_new, name='post_new'),
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
    path('drafts/', views.post_draft_list, name='post_draft_list'),
    path('post/<int:pk>/publish', views.publish, name='post_publish'),
    path('post/<int:pk>/remove', views.remove, name='post_remove'),
    path('category/<int:pk>/show', views.category_search, name='category_search')
]

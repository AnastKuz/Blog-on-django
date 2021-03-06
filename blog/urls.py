from django.conf.urls import url
from django.urls import path

from . import views
from .views import HomeView, PostDetailView, AddPostView, UpdatePostView, DeletePostView

urlpatterns = [
    path('', HomeView.as_view(), name="home"),
    path('post/<int:pk>', PostDetailView.as_view(), name="detail"),
    path('post/edit/<int:pk>', UpdatePostView.as_view(), name="edit"),
    path('post/<int:pk>/delete/', DeletePostView.as_view(), name="delete"),
    path('add/', AddPostView.as_view(), name="add"),
    url(r'^list$', views.post_list, name="list"),
]

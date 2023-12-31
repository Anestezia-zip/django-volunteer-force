from . import views
from django.urls import path


urlpatterns = [
    path('', views.AllPostsView.as_view(), name='home'),
    path('post/<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
    path('profile/', views.UserPostsView.as_view(), name='profile'),
    path('edit_profile/', views.edit_profile, name='edit_profile'),
    path('donate/', views.donate, name='donate'),
    path('map/', views.map, name='map'),
]

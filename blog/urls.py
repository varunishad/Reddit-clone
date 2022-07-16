from django.urls import path, include
from . import views
# from .views import like_view


urlpatterns = [
    path('home/', views.home, name='home'),
    path('create/', views.create, name= 'create'),
    path('myprofile/<str:username>', views.myprofile, name='myprofile'),
    path('search_results', views.search, name='searches'),
    path('<int:pk>/delete', views.delete, name='delete_post'),
    path('like/', views.likes, name='likes'),
    path('dislike/', views.likes, name='dislikes'),
    path('post/<int:pk>', views.comment, name='post_comment')
    # path('like/<int:pk>', like_view, name='like_post'),

]

